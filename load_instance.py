# coding:utf-8
import dataclasses
import json
from dataclasses import dataclass


@dataclass(init=False)
class Instance(object):
    instance_name: str
    planning_horizon: int
    horizon_list: list
    scenario_list: list
    scenario_num: int

    affected_list: list
    affected_node_num: int
    affected_capacity: dict
    affected_population: dict
    affected_demand: dict

    exponential_deprivation_cost_parameters: (float, float)
    deprivation_cost: dict
    deprivation_cost_scale: float
    deprivation_cost_upper_limit: float

    facility_num: int
    facility_list: list
    facility_capacity: dict
    relief_item_unit_cost: float

    phc_num: int
    phc_list: list
    phc_unit_cost: dict
    phc_lead_time: dict
    phc_alpha: dict
    phc_beta: dict
    phc_ability: dict

    prc_num: int
    prc_list: list
    prc_unit_cost: dict
    prc_first_lead_time: dict
    prc_lead_time: dict
    prc_ability: dict

    location_id_name_map: dict
    instance_type: str

    def __init__(self, **instance_data):
        for f in dataclasses.fields(self):
            if f.name in instance_data.keys():
                setattr(self, f.name, instance_data[f.name])
            else:
                setattr(self, f.name, None)
        self.instance_type = "case_study" if instance_data.get("instance_type") == "case_study" else "synthetic"


def read_instance(file_path):
    # .JSON file -> Python dictionary
    with open(file_path + ".json", 'r') as f:
        lines = f.read()
    dict_obj = json.loads(
        lines,
        object_hook=lambda d: {int(k) if k.lstrip('-').isdigit() else k: v for k, v in d.items()}
    )
    return dict_obj


if __name__ == '__main__':
    # Replace "case_national" with "case_state" or "05-03-0", ...
    instance_name = "case_state"
    instance_data = read_instance(instance_name)
