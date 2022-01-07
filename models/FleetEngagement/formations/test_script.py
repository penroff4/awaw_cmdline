from TaskForce import TaskForce

combatants_dict = {0:{"short_designation": "test", "NATIONALITY": "TEST", "fleet_composition":[]}}

test_tf = TaskForce("TEST", 0, "UNINVERTED", "FAST")

test_tf.taskforceComposition(combatants_dict, 0, 0)