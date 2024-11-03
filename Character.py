class Character:
    def __init__(self, name, weight, acceleration, top_speed, handling, ci, vl, dp, kb, rr, on_road_traction, mini_turbo):
        self.name = name
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

        self.on_road_traction = on_road_traction
        self.mini_turbo = mini_turbo

    # Getter methods
    def get_name(self):
        return self.name
    
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

    def get_on_road_traction(self):
        return self.on_road_traction

    def get_mini_turbo(self):
        return self.mini_turbo
 
    def add_powerup(self, powerup):
        self.powerups.append(powerup) 

    def get_powerups(self):
        powerup_names = []
        for pu in self.powerups:
            powerup_names.append(pu.get_name())

        return powerup_names
    
    def set_win_stat(self, win_change):
        self.win_stat += win_change

    def __str__(self):
        return str(self.weight)
