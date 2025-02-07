
import scipy.stats as stats

class SignalDetection:
    def __init__(self, hits, misses, false_alarms, correct_rejections):
       
        self.hits = hits
        self.misses = misses
        self.false_alarms = false_alarms
        self.correct_rejections = correct_rejections
   
    def hit_rate(self): 
        """Calculate hit rate (H) """
        total_signals = self.hits + self.misses
        H = self.hits / total_signals if total_signals > 0 else 0.0001
        return min(max(H, 0.0001), 0.9999)
   
    def false_alarm_rate(self):
        """Calculate flase alarm rate (FA)"""
