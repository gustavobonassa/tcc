from adaptive_xgboost import AdaptiveXGBoostClassifier
# from adaptive_incremental_ensemble import AdaptiveXGBoostClassifier2
# from adaptive_incremental import Adaptive2
# from adaptive_xgboost_thread import Adaptive3
# from adaptive_incremental2 import Adaptive4
from adaptive_semiV2 import AdaptiveSemi

from skmultiflow.data import ConceptDriftStream
from skmultiflow.evaluation import EvaluatePrequential
from skmultiflow.data.file_stream import FileStream
from skmultiflow.data.random_tree_generator import RandomTreeGenerator
from skmultiflow.data import SEAGenerator
from skmultiflow.data import AGRAWALGenerator
from skmultiflow.meta import AdaptiveRandomForestClassifier
from skmultiflow.data.hyper_plane_generator  import HyperplaneGenerator

# Adaptive XGBoost classifier parameters
n_estimators = 30       # Number of members in the ensemble
learning_rate = 0.05     # Learning rate or eta
max_depth = 5           # Max depth for each tree in the ensemble
max_window_size = 10000  # Max window size
min_window_size = 1     # set to activate the dynamic window strategy
detect_drift = False    # Enable/disable drift detection
ratio_unsampled = 0
small_window_size = 150

max_buffer = 25
pre_train = 15

## autor push
# AXGBp = AdaptiveXGBoostClassifier(update_strategy='push',
#                                   n_estimators=n_estimators,
#                                   learning_rate=learning_rate,
#                                   max_depth=max_depth,
#                                   max_window_size=max_window_size,
#                                   min_window_size=min_window_size,
#                                   detect_drift=detect_drift)
## meu ensemble incremental
# AXGBp2 = AdaptiveXGBoostClassifier2(update_strategy='push',
#                                   n_estimators=n_estimators,
#                                   learning_rate=learning_rate,
#                                   max_depth=max_depth,
#                                   max_window_size=max_window_size,
#                                   min_window_size=min_window_size,
#                                   detect_drift=detect_drift)
## autor replace
AXGBr = AdaptiveXGBoostClassifier(update_strategy='replace',
                                  n_estimators=n_estimators,
                                  learning_rate=learning_rate,
                                  max_depth=max_depth,
                                  max_window_size=max_window_size,
                                  min_window_size=min_window_size,
                                  detect_drift=detect_drift,
                                  ratio_unsampled=ratio_unsampled)

## meu incremental
# AXGBg = Adaptive4(learning_rate=learning_rate,
#                                   max_depth=max_depth,
#                                   max_window_size=max_window_size,
#                                   min_window_size=min_window_size,
#                                   ratio_unsampled=ratio_unsampled)

AXGBg2 = AdaptiveSemi(learning_rate=learning_rate,
                                  max_depth=max_depth,
                                  max_window_size=max_window_size,
                                  min_window_size=min_window_size,
                                  ratio_unsampled=ratio_unsampled,
                                  small_window_size=small_window_size,
                                  max_buffer=max_buffer,
                                  pre_train=pre_train)

# ## meu thread
# AXGBt = Adaptive3(n_estimators=n_estimators,
#                                   learning_rate=learning_rate,
#                                   max_depth=max_depth,
#                                   max_window_size=max_window_size,
#                                   min_window_size=min_window_size,
#                                   detect_drift=detect_drift)

stream = SEAGenerator(noise_percentage=0.1)
# stream = FileStream("./datasets/elec.csv")
# stream = RandomTreeGenerator(n_num_features=200)
# stream = ConceptDriftStream(random_state=1,
#                             position=50000)
# stream = RandomTreeGenerator(tree_random_state=23, sample_random_state=12, n_classes=2, n_cat_features=2,
#                                  n_num_features=5, n_categories_per_cat_feature=5, max_tree_depth=6, min_leaf_depth=3,
#                                  fraction_leaves_per_level=0.15)
# stream.prepare_for_use()   # Required for skmultiflow v0.4.1


# classifier = SGDClassifier()
# classifier2 = KNNADWINClassifier(n_neighbors=8, max_window_size=2000,leaf_size=40, nominal_attributes=None)
# classifier3 = OzaBaggingADWINClassifier(base_estimator=KNNClassifier(n_neighbors=8, max_window_size=2000,
#                                         leaf_size=30))
# classifier4 = PassiveAggressiveClassifier()
# classifier5 = SGDRegressor()
# classifier6 = PerceptronMask()
# arf = AdaptiveRandomForestClassifier()


# for i in range(30):
evaluator = EvaluatePrequential(pretrain_size=0,
                                max_samples=200000,
                                # batch_size=1,
                                show_plot=False,
                                metrics=["accuracy","running_time"])
# fileName = "seaAXGBr"+str(i)+".csv"
# print(fileName)
evaluator.evaluate(stream=stream,
                  #  model=[AXGBg2],
                  # output_file=fileName,
                  model=[AXGBg2],
                  model_names=["AXGB adaptado"])
