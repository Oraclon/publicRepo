from ControlThreadWithObserver import MainThread

for i in range(6):
    thr = MainThread(count=i)
    thr.start()
