# Dataset of “*Capacity reservation for humanitarian relief: A logic-based Benders decomposition method with subgradient cut*”

This repository is the dataset associated with the paper  `Guo, P., & Zhu, J. (2023). Capacity reservation for humanitarian relief: A logic-based Benders decomposition method with subgradient cut. European Journal of Operational Research. https://doi.org/10.1016/j.ejor.2023.06.006`

This dataset consistent of two parts:

- [`**-**-*.json`] Synthetic data generated in this paper.
- [`case_national/state.json`] Real-world case study data adapted from *Veloso, R., Cespedes, J., Caunhye, A., & Alem, D. (2022). Brazilian disaster datasets and real-world instances for optimization and machine learning. Data in Brief, 42, 108012. https://doi.org/10.1016/j.dib.2022.108012*.

Cite this dataset use

```
@article{guoCapacityReservationHumanitarian2023,
  title={Capacity reservation for humanitarian relief: A logic-based Benders decomposition method with subgradient cut},
  author={Guo, Penghui and Zhu, Jianjun},
  year={2023},  
  journal = {European Journal of Operational Research},
  volume = {***},
  number = {*},
  pages = {***--***},
  doi = {10.1016/j.ejor.2023.06.006}
}
```

Instances in this dataset is saved in `.JSON` format, and the Python code `load_instance.py` is provided for loading instances.  Attributes in the .JSON files are described as bellow. Before using this dataset, it is __HIGHLY__ recommended to read our and Veloso et al‘s papers first.


|  Attributes | Type | Description  |
| ------ | ------ |--------------|
| instance_name | str | Name of the instance |
| planning_horizon | int | Length of planning horizon |
| horizon_list | list | List of response phases |
| scenario_list | list | List of scenarios |
| scenario_num | int | Number of scenarios |
| __Affected communities__ |  |              |
| affected_list | list | List of affected communities |
| affected_node_num | int | Number of affected community |
| affected_capacity | dict | Capacity of each affected community |
| affected_population | dict | Population of each affected community* |
| affected_demand | dict | __[Stochastic]__ Demand of each affected community |
| __Deprivation cost__ |  |              |
| exponential_deprivation_cost_parameters | tuple | The deprivation function is   $v1 \cdot e^{v2 \cdot t}$ |
| deprivation_cost | dict | Deprivation cost that can be incurred for certain length of shortage |
| deprivation_cost_scale | float | Values in `deprivation_cost` should divided by `deprivation_cost_scale` |
| deprivation_cost_upper_limit | float | Value of life |
| __Relief facility__ |  |              |
| facility_num | int | Number of relief facility |
| facility_list | list | List of relief facilities |
| facility_capacity | dict | Capacity of each relief facility |
| relief_item_unit_cost | float | Unit cost for prepositioning relief item |
| __Physical capacity reservation (PHCR)__ |  |              |
| phc_num | int | Number of PHCR suppliers |
| phc_list | list | List of PHCR suppliers |
| phc_unit_cost | dict | Unit acquiring cost from each PHCR supplier |
| phc_lead_time | dict | Lead time orders from each PHCR supplier |
| phc_alpha | dict | Quantity flexibility contract parameter $\alpha$ |
| phc_beta | dict | Quantity flexibility contract parameter $\beta$ |
| phc_ability | dict | Maximum order sizes from each PHCR supplier |
| __Production capacity reservation (PRCR)__ |  |              |
| prc_num | int | Number of PRCR suppliers |
| prc_list | list | List of PRCR suppliers |
| prc_unit_cost | dict | Unit acquiring cost from each PRCR supplier |
| prc_first_lead_time | dict | __[Stochastic]__ Lead time of the first order from each PRCR supplier |
| prc_lead_time | dict | Lead time of the second and following orders from each PRCR supplier |
| prc_ability | dict | Maximum order sizes from each PRCR supplier |
| __Others__ |  |              |
| location_id_name_map | dict | Mapping from affected community ID to name (only applied to `case_study` instances) |
| instance_type | str | Type of the instance (`synthetic` or `case_study`) |

**Note that in `case_study` instances, `affected_population` is scenario-dependent; while in `synthetic` instances, `affected_population` is deterministic.*

If you have any question, please contact *Penghui Guo*.
