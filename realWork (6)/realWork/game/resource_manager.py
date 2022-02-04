import pygame as pg

class ResourceManager:


    def __init__(self):

        # resources
        self.resources = {
            "wood": 10,
            "stone": 10,
            "meat":0
        }

        #costs
        self.costs = {
            "Castle": {"wood": 7, "stone": 3},
            "House": {"wood": 3, "stone": 5},
            "Mining": {"wood": 3, "stone": 5},
            "Wood": {"wood": 3, "stone": 5},
        }

    def apply_cost_to_resource(self, building):
        for resource, cost in self.costs[building].items():
            self.resources[resource] -= cost

    def is_affordable(self, building):
        affordable = True
        for resource, cost in self.costs[building].items():
            if cost > self.resources[resource]:
                affordable = False
        return affordable
