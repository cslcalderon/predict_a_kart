class Character:
    def __init__(self, weight, acceleration, top_speed, handling, ci, vl, dp, kb, rr):
        self.weight = weight
        self.acceleration = acceleration
        self.top_speed = top_speed
        self.handling = handling
        self.map_perf = {
            "choco_island": ci,
            "vanilla_lake": vl,
            "donut_plains": dp,
            "koopa_beach": kb,
            "rainbow_road": rr
        }
        self.powerups = []
        self.win_stat = 0

    # Getter methods
    def get_weight(self):
        return self.weight

    def get_acceleration(self):  
        return self.acceleration

    def get_top_speed(self):
        return self.top_speed

    def get_handling(self):
        return self.handling

    def get_map_perf(self, map_name):
        return self.map_perf.get(map_name, None)  
    
    def set_win_stat(self, win_change):
        self.win_stat += win_change

    def __str__(self):
        return str(self.weight)
