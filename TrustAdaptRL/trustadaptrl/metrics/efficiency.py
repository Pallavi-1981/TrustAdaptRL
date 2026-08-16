import os,time,psutil
class EfficiencyMeter:
    def __init__(self): self.proc=psutil.Process(os.getpid())
    def measure(self,fn,*args,**kwargs):
        mem0=self.proc.memory_info().rss/1024**2; cpu0=self.proc.cpu_times().user; t0=time.perf_counter(); out=fn(*args,**kwargs); dt=(time.perf_counter()-t0)*1000; cpu1=self.proc.cpu_times().user; mem1=self.proc.memory_info().rss/1024**2
        return out, {'decision_latency_ms':dt,'memory_delta_mb':mem1-mem0,'cpu_user_seconds':cpu1-cpu0}
def estimated_energy_mj(latency_ms,power_watts=1.5): return float(power_watts*latency_ms)
