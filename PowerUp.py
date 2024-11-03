class PowerUp():
    def __init__(self, name, ci, vl, dp, kb, rr, speed_related):
        self.name = name
        self.ci = ci
        self.vl = vl
        self.dp = dp
        self.kb = kb
        self.rr = rr
        self.speed_related = speed_related
        self.probabilities = {'choco_island': ci, 'vanilla_lake': vl, 'donut_plains': dp, \
                              'koopa_beach': kb, 'rainbow_road': rr}
    
    def get_name(self):
        return self.name
    
    def get_ci(self):
        return self.ci
    
    def get_vl(self):
        return self.vl
    
    def get_dp(self):
        return self.dp
    
    def get_kb(self):
        return self.kb
    
    def get_rr(self):
        return self.rr
    
    def get_speed_related(self):
        return self.speed_related
    
    def get_probability_for_map(self, map_name):
        return self.probabilities.get(map_name, 0) / 7
        