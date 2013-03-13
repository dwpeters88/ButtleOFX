from PySide import QtCore, QtGui
# tools
from buttleofx.data import tuttleTools
# quickmamba
from quickmamba.patterns import Singleton, Signal


class ButtleEvent(QtCore.QObject):
    """
        Class ButtleEvent defined by:
            - paramChangedSignal : signal emited when a param value changed
            - viewerChangedSignal : signal emited when ???

        This class contains all data we need to manage the application.
    """

    # signals
    oneParamChangedSignal = Signal()
    viewerChangedSignal = Signal()

    ### flag ###

    def canPaste(self):
        """
            Returns true if we can paste (= if there was at least one node selected)
        """
        return self._currentCopiedNodesInfo != {}

    ### emit signals ###

    def emitOneParamChangedSignal(self):
        """
            Emit paramChangedSignal.
        """
        self.oneParamChangedSignal()

    def emitViewerChangedSignal(self):
        """
            Emit viewerChangedSignal.
        """
        self.viewerChangedSignal()

    ################################################## DATA EXPOSED TO QML ##################################################

    # paste possibility
    pastePossibilityChanged = QtCore.Signal()
    canPaste = QtCore.Property(bool, canPaste, notify=pastePossibilityChanged)


# This class exists just because thre are problems when a class extends 2 other class (Singleton and QObject)
class ButtleEventSingleton(Singleton):

    _buttleEvent = ButtleEvent()

    def get(self):
        return self._buttleEvent