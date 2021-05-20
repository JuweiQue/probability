# Lint as: python3
# Copyright 2021 The TensorFlow Probability Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# pylint: disable=line-too-long
r"""Synthetic dataset generated from the PlasmaSpectroscopy model.

This was generated using the following snippet:

```python
import tensorflow.compat.v2 as tf
tf.enable_v2_behavior()

import tensorflow_probability as tfp
from inference_gym.internal import array_to_source
from inference_gym import using_tensorflow as gym
import numpy as np

num_sensors = 40
num_wavelengths = 40
wavelengths = np.linspace(0.01, 0.2, num_wavelengths)
center_wavelength = wavelengths.mean()

model = gym.targets.PlasmaSpectroscopy(
    tf.zeros((num_wavelengths, num_sensors)),
    wavelengths=wavelengths,
    center_wavelength=center_wavelength)
sample, dataset = model._sample_dataset(seed=(0, 8))

sources = []
for k, v in sample._asdict().items():
  sources.append(
    array_to_source.array_to_source(
        k.upper(), v))

for k, v in dataset.items():
  sources.append(
    array_to_source.array_to_source(
        k.upper(), v))

with open('/tmp/synthetic_plasma_spectroscopy.py', 'w') as f:
  f.write("\n\n".join(sources))
```

Note that the final `_sample_dataset` is not reproducible, hence the output is
checked in.

"""

import numpy as np

AMPLITUDE = np.array([
    1.4802036,
    1.8915913,
    -0.011120212,
    1.1328301,
    1.2841645,
    0.6033605,
    -1.887041,
    -2.012894,
    0.046582267,
    1.5555662,
    0.4305847,
    -1.7179363,
    -1.1399889,
    -0.4432812,
    -1.4721184,
    0.35457477,
]).reshape((16,))


TEMPERATURE = np.array([
    1.2321296,
    -0.020694781,
    -1.3441145,
    -0.51342154,
    -0.6282792,
    -0.22180416,
    -1.0089059,
    1.4475185,
    -1.8519154,
    0.5540126,
    -1.3644233,
    1.5542297,
    -0.4033564,
    -0.029513652,
    -0.14812116,
    0.93214256,
]).reshape((16,))


VELOCITY = np.array([
    0.010279292,
    -1.6109133,
    0.85784495,
    0.8826037,
    0.19365458,
    -0.36963812,
    1.2059057,
    -0.93545884,
    0.38819882,
    1.6983186,
    -1.8130875,
    0.94406796,
    -0.79738003,
    -1.0478632,
    -0.38848934,
    -0.48529625,
]).reshape((16,))


SHIFT = np.array([
    -0.5514385,
]).reshape(())


WAVELENGTHS = np.array([
    0.01,
    0.014871794871794873,
    0.019743589743589744,
    0.024615384615384615,
    0.029487179487179487,
    0.03435897435897436,
    0.039230769230769236,
    0.04410256410256411,
    0.04897435897435898,
    0.05384615384615385,
    0.05871794871794872,
    0.06358974358974359,
    0.06846153846153846,
    0.07333333333333333,
    0.0782051282051282,
    0.08307692307692308,
    0.08794871794871795,
    0.09282051282051282,
    0.09769230769230769,
    0.10256410256410256,
    0.10743589743589743,
    0.1123076923076923,
    0.11717948717948717,
    0.12205128205128205,
    0.12692307692307694,
    0.13179487179487182,
    0.1366666666666667,
    0.14153846153846156,
    0.14641025641025643,
    0.1512820512820513,
    0.15615384615384617,
    0.16102564102564104,
    0.1658974358974359,
    0.17076923076923078,
    0.17564102564102566,
    0.18051282051282053,
    0.1853846153846154,
    0.19025641025641027,
    0.19512820512820514,
    0.2,
]).reshape((40,))


CENTER_WAVELENGTH = np.array([
    0.10500000000000001,
]).reshape(())


MEASUREMENTS = np.array([
    -0.66101485,
    0.31644753,
    -0.5896422,
    0.4764485,
    2.1545932,
    15.793148,
    8.2264805,
    6.457074,
    5.7062893,
    6.1811686,
    8.777044,
    6.9074125,
    7.9522552,
    7.701313,
    8.559349,
    8.296498,
    6.1969037,
    6.4804926,
    6.8852997,
    8.830744,
    14.376627,
    0.54612935,
    0.124028,
    0.44405863,
    0.5131382,
    0.5987899,
    0.008983987,
    -0.24756075,
    0.7618118,
    -0.21146192,
    0.4546959,
    0.09494688,
    -0.26813537,
    0.5798886,
    -0.10784844,
    0.18372172,
    0.8161483,
    -0.3787802,
    0.61460984,
    -0.41957632,
    0.13647377,
    -0.3481221,
    0.03326019,
    1.7144626,
    3.8620698,
    14.40822,
    9.046495,
    7.6838465,
    7.2554746,
    8.057631,
    11.189637,
    9.038466,
    8.125581,
    8.294034,
    10.172681,
    11.90528,
    7.1925435,
    6.708079,
    7.6085744,
    9.414239,
    14.608672,
    1.5265317,
    1.09792,
    0.29970562,
    0.29824358,
    0.36030084,
    -0.37960574,
    0.47860667,
    0.91203105,
    -0.6904322,
    -0.2722036,
    0.23733543,
    -0.6658274,
    0.62095886,
    0.73466265,
    -0.8475226,
    -0.1700871,
    0.9261157,
    0.422822,
    0.32836267,
    0.58122945,
    -0.83155084,
    -0.20049855,
    -0.040298104,
    4.014356,
    16.160791,
    7.2828264,
    7.3377733,
    6.665611,
    8.653453,
    11.973017,
    9.656379,
    10.9801235,
    9.05112,
    10.565474,
    11.942185,
    7.2904882,
    7.4630857,
    6.514908,
    9.644132,
    14.969957,
    0.07107994,
    0.11467081,
    0.92357284,
    0.04355552,
    0.6726098,
    -0.15279476,
    0.713554,
    0.5466241,
    -0.38109347,
    0.5590394,
    0.08306945,
    0.9525252,
    0.6713458,
    0.51892877,
    -0.1279359,
    -0.15663871,
    0.020156374,
    -0.060285714,
    -1.0264076,
    -0.53699505,
    -0.9786586,
    0.015289649,
    1.5724823,
    4.0689135,
    13.646254,
    8.417458,
    7.3368583,
    6.966266,
    8.73208,
    14.498494,
    10.2102165,
    11.423929,
    11.351579,
    12.9430065,
    15.01266,
    9.051174,
    7.077483,
    6.785291,
    9.483119,
    15.76488,
    1.1677985,
    1.6693239,
    -0.21604359,
    0.32284033,
    -0.22243214,
    0.60323435,
    -0.11199745,
    0.29957047,
    0.006062749,
    0.7996792,
    0.3094816,
    -0.7718058,
    0.503415,
    0.07231447,
    -0.2853677,
    0.4330218,
    0.844616,
    -0.19574685,
    -0.3879851,
    0.5901966,
    0.051313907,
    -0.29432508,
    1.2537544,
    3.1426716,
    14.615546,
    8.347049,
    7.4366584,
    6.4491363,
    9.865336,
    15.843064,
    12.469691,
    11.894229,
    12.133173,
    14.63979,
    16.16245,
    9.504371,
    8.017702,
    7.867693,
    9.518961,
    14.380217,
    0.66953653,
    0.60293055,
    0.00082825124,
    -0.28320992,
    0.8367502,
    0.12513764,
    0.22053392,
    -0.10229007,
    -0.20082277,
    0.63717407,
    0.32739908,
    -0.093239225,
    -0.80318755,
    0.9917766,
    0.24838758,
    -0.07330545,
    0.15537623,
    0.09008534,
    -0.06607497,
    1.0962121,
    0.55644095,
    0.6913326,
    0.9021442,
    3.8921309,
    14.102233,
    7.184174,
    7.315026,
    7.334084,
    10.787065,
    19.485243,
    13.958044,
    14.3500805,
    13.616628,
    15.63192,
    17.07027,
    9.131023,
    6.8167133,
    6.970449,
    8.922994,
    14.361785,
    1.7793398,
    0.94775784,
    0.105669454,
    -0.18747061,
    0.6676264,
    -0.3883816,
    -0.6202498,
    -0.0833843,
    -0.5216094,
    1.1268811,
    -0.59910476,
    0.39042526,
    0.47714886,
    -0.7111677,
    -0.5756576,
    0.9333002,
    0.1010186,
    0.13677923,
    -0.75147396,
    1.2583244,
    -0.23063457,
    0.7901664,
    0.24705392,
    3.6259048,
    12.530731,
    6.9297647,
    7.079164,
    7.2256374,
    11.940973,
    20.025602,
    14.700426,
    13.519883,
    14.241193,
    17.55714,
    17.386055,
    10.167002,
    7.536337,
    7.0136056,
    9.326938,
    12.228463,
    0.17775005,
    0.8319777,
    -0.8991761,
    -0.01412341,
    0.61705685,
    -0.14188325,
    -0.41435227,
    -0.316557,
    -0.5893145,
    -0.010637931,
    0.20675054,
    0.44020182,
    -0.7080041,
    0.16052538,
    -0.48142046,
    0.9052833,
    0.432698,
    0.03338314,
    0.35594848,
    1.1689888,
    0.36019892,
    0.23971666,
    1.4662509,
    3.3352752,
    11.360069,
    8.300535,
    7.5611286,
    7.2111707,
    17.327162,
    20.148909,
    17.380922,
    17.596447,
    14.160338,
    19.188683,
    17.219112,
    10.499862,
    8.309862,
    6.1963353,
    7.3864193,
    12.878287,
    1.4184926,
    1.7496321,
    -0.082713336,
    0.23216072,
    0.20258206,
    1.0141679,
    0.14271286,
    -0.29340488,
    -0.055605985,
    -0.5336929,
    -0.54352623,
    0.19902669,
    0.12139763,
    -0.018293247,
    -0.20558693,
    -0.8606704,
    0.22833318,
    0.4463366,
    0.20494421,
    0.7066752,
    -0.62247527,
    0.117985666,
    1.831157,
    3.299585,
    9.63925,
    7.483565,
    7.1289496,
    6.4751153,
    15.985568,
    21.507505,
    18.539736,
    16.699535,
    16.726501,
    19.698357,
    22.443224,
    11.952675,
    7.005475,
    6.2864413,
    8.778635,
    10.89195,
    0.66351974,
    1.1440128,
    -0.25076824,
    0.66586065,
    1.0526825,
    0.015522989,
    0.07891381,
    1.104366,
    0.7747889,
    0.15351877,
    -0.12182697,
    -0.59052014,
    -0.12581429,
    0.5053382,
    0.17305401,
    0.67090386,
    1.036633,
    0.05909565,
    0.28418896,
    0.86726683,
    0.1763895,
    0.33444333,
    1.7197226,
    2.5705223,
    9.934082,
    6.614648,
    5.9702163,
    7.0940704,
    18.322672,
    24.886862,
    18.648033,
    19.174364,
    17.071978,
    18.935146,
    20.495438,
    13.39125,
    7.1744776,
    5.476832,
    7.2689962,
    10.46958,
    1.1804211,
    1.0994785,
    0.64040864,
    0.021063149,
    0.75519574,
    0.40024444,
    -0.48553574,
    0.87461084,
    -0.23675112,
    0.1914608,
    -0.49892142,
    0.2618199,
    0.6261685,
    -1.4913763,
    0.41756257,
    0.5763335,
    -0.45616063,
    0.38227928,
    -0.6692691,
    1.8232274,
    0.7977414,
    0.40125495,
    2.787939,
    3.2074018,
    8.831141,
    6.6602535,
    7.500632,
    8.793667,
    18.995548,
    23.698793,
    18.186054,
    17.543282,
    18.392523,
    20.788607,
    24.634804,
    14.188387,
    8.168461,
    5.5740485,
    6.8008204,
    8.531001,
    1.4529983,
    2.276989,
    1.0289037,
    0.9468033,
    -0.038641334,
    -0.39401633,
    -1.1387177,
    0.49660775,
    0.5171432,
    -0.6254447,
    1.2226907,
    -0.13812594,
    0.11419458,
    -0.36041245,
    0.16572447,
    -0.2501292,
    -0.95744544,
    0.6987992,
    0.3099944,
    1.108943,
    0.41807377,
    1.350997,
    1.2673455,
    3.2821457,
    8.0927515,
    5.9851384,
    4.8361425,
    8.642136,
    20.54146,
    23.320255,
    20.936903,
    19.881096,
    18.084406,
    20.986282,
    22.538109,
    15.849695,
    7.59143,
    5.759286,
    7.9955835,
    7.542832,
    1.5869404,
    2.191163,
    -0.0054766536,
    0.38372415,
    1.4580531,
    -0.6341528,
    -0.20307654,
    -0.82046396,
    0.30573404,
    0.59632486,
    -0.12896755,
    -0.42806864,
    -0.47942856,
    -0.7036555,
    0.075889945,
    0.29308736,
    -1.4974035,
    -0.036708307,
    -0.43896213,
    0.54672736,
    1.3562044,
    1.5058006,
    2.0175235,
    3.2622445,
    7.817541,
    6.1968045,
    5.7298784,
    8.535798,
    22.878216,
    23.569859,
    21.438442,
    20.779306,
    18.338245,
    23.335554,
    23.656643,
    16.534071,
    7.0056953,
    5.3699074,
    6.2035737,
    6.91238,
    1.8461741,
    2.0328891,
    0.6284174,
    0.07324934,
    0.72266495,
    0.43248987,
    0.55657876,
    -0.36850226,
    0.2892055,
    0.120979175,
    -0.3255677,
    0.18210961,
    -0.13677588,
    -0.79952997,
    -0.16948017,
    0.27382505,
    0.011414817,
    -0.002753294,
    0.1875501,
    1.7294772,
    0.86453336,
    0.8789885,
    2.0237687,
    2.686733,
    7.0931683,
    6.7965593,
    5.703301,
    9.106176,
    19.852842,
    22.134148,
    24.209602,
    20.48003,
    19.87589,
    22.650255,
    24.67572,
    17.161873,
    7.185769,
    5.12218,
    5.9893394,
    5.907269,
    2.1844404,
    1.9687537,
    1.0286644,
    0.052360654,
    1.7644687,
    0.5339646,
    -0.53046066,
    -0.2281848,
    -1.2462859,
    0.6778776,
    0.5408989,
    -0.14820653,
    0.38658077,
    -0.65733767,
    0.014478714,
    0.45866382,
    0.47466084,
    0.48330665,
    0.52647215,
    1.6572766,
    -0.093874216,
    1.0939939,
    2.8252633,
    3.250628,
    7.286972,
    5.736179,
    5.5879693,
    9.545634,
    22.925808,
    23.213871,
    23.39594,
    21.748808,
    22.024412,
    24.974943,
    23.57301,
    18.065563,
    8.397812,
    4.8709254,
    7.626314,
    4.6410003,
    1.8595266,
    3.0831103,
    1.4402436,
    1.2672244,
    1.312456,
    -0.18201214,
    0.21097422,
    -0.026861114,
    0.18476872,
    0.7252849,
    -0.002409873,
    -0.29303908,
    1.3546691,
    -0.04322617,
    -0.053203642,
    -0.30067968,
    -0.12050266,
    -0.5528519,
    0.057745364,
    1.3053449,
    1.8519605,
    1.8503615,
    2.5469666,
    4.2060847,
    5.5301046,
    7.0553675,
    5.9386334,
    11.875089,
    23.438046,
    20.363987,
    23.725615,
    20.967691,
    21.432257,
    24.202627,
    19.774887,
    18.783188,
    7.98809,
    6.2239876,
    7.760503,
    5.212336,
    2.9735184,
    2.7213335,
    2.0156252,
    1.814288,
    2.2770615,
    0.01533184,
    0.58220863,
    -0.49351138,
    0.31417957,
    -0.36469758,
    0.45743746,
    0.66627234,
    0.3081961,
    0.828259,
    -0.31382263,
    0.26520026,
    0.22944771,
    -0.6709603,
    -0.07570245,
    1.5327783,
    1.7784487,
    2.6468341,
    3.198592,
    3.7656205,
    5.9252257,
    6.9020658,
    4.9581833,
    12.047751,
    22.348654,
    20.17518,
    24.174393,
    21.535011,
    19.05106,
    22.163195,
    21.497072,
    18.43445,
    8.682917,
    5.3132563,
    7.030179,
    3.717919,
    2.0626392,
    2.4575338,
    2.2717822,
    0.8625143,
    2.4770658,
    -0.786061,
    1.2881083,
    -0.2518999,
    0.72405684,
    -0.122574806,
    -0.34197915,
    0.13918422,
    0.26873538,
    -0.47515658,
    -0.54810023,
    0.89566797,
    -0.54384357,
    -0.12311963,
    0.567525,
    2.7046611,
    1.5512958,
    1.7786896,
    3.8791292,
    3.9559023,
    4.788476,
    8.228316,
    5.3946,
    12.281274,
    21.967098,
    20.923243,
    23.913458,
    20.710938,
    19.420635,
    25.138704,
    18.289383,
    19.177135,
    8.415327,
    4.8929396,
    8.965305,
    4.3885813,
    3.4578655,
    3.0384607,
    1.5863328,
    1.91974,
    2.4258208,
    0.5892152,
    0.048560977,
    -0.13528748,
    -0.21397328,
    0.16264682,
    -0.57951355,
    -0.40301454,
    0.21641892,
    -0.22450455,
    0.38177252,
    -0.967473,
    -0.35485935,
    0.062246032,
    -0.03395147,
    2.1338463,
    1.9084859,
    3.1863737,
    1.9375713,
    3.4518764,
    6.570703,
    6.878443,
    5.679476,
    13.351213,
    22.931889,
    19.282558,
    22.36135,
    23.796984,
    21.032475,
    23.09803,
    20.966232,
    20.72223,
    6.7338567,
    6.4885483,
    7.190284,
    4.9310346,
    3.1236634,
    3.5150487,
    2.9693668,
    2.2454295,
    1.82249,
    -0.09966546,
    0.72314006,
    -0.79027426,
    0.41793302,
    -0.14793015,
    0.45988762,
    0.8456978,
    -0.5273398,
    0.1830612,
    -1.0828326,
    -1.0117317,
    -0.3019783,
    0.17001551,
    -0.62556803,
    2.961217,
    2.6823378,
    2.9682546,
    5.2445164,
    4.9527783,
    6.309333,
    7.7392774,
    6.2129936,
    15.35368,
    20.683935,
    20.589102,
    22.10926,
    20.185204,
    20.562426,
    22.645317,
    18.869568,
    20.659521,
    8.880328,
    6.4410696,
    9.769155,
    5.5935693,
    5.527752,
    4.5683465,
    3.4019177,
    3.3163903,
    2.244741,
    0.38402623,
    0.2960868,
    -0.4828044,
    0.13759217,
    0.25681636,
    0.11657055,
    -0.330115,
    0.4011577,
    -0.7654019,
    0.14916949,
    -0.6228205,
    -0.96823233,
    -0.022868,
    -0.49047035,
    3.20636,
    2.6912642,
    2.9050756,
    4.912674,
    5.7441964,
    6.489336,
    9.632326,
    6.2825303,
    16.68777,
    21.077969,
    17.172966,
    18.92938,
    23.38385,
    20.251026,
    22.16378,
    18.001736,
    20.24098,
    11.019654,
    6.6073513,
    8.655663,
    6.298364,
    6.4654784,
    3.6983974,
    3.1087956,
    2.226927,
    2.6668777,
    -0.35526595,
    1.4488825,
    0.20488043,
    0.047601122,
    -0.6924504,
    0.57495445,
    0.5399022,
    -0.47663862,
    0.8161736,
    -0.36598107,
    -0.59101355,
    0.20327158,
    0.41677478,
    0.27029967,
    3.7847342,
    3.2484818,
    3.747693,
    4.7734656,
    6.716756,
    8.185982,
    9.418276,
    7.493696,
    14.704602,
    17.729408,
    17.48148,
    19.855602,
    20.371563,
    18.5821,
    18.155266,
    16.968113,
    17.100256,
    10.015516,
    7.8247633,
    8.993816,
    6.4911056,
    6.2132425,
    4.3434267,
    3.7000012,
    3.7377622,
    3.1024928,
    -0.30869377,
    0.051026687,
    -0.34078225,
    0.7479868,
    0.03696166,
    -0.75611556,
    1.1542099,
    -0.028129257,
    0.08181842,
    0.09559424,
    0.8364861,
    0.096545294,
    0.5584201,
    -0.5194905,
    3.589691,
    4.05453,
    3.794124,
    4.707637,
    9.231918,
    8.564278,
    9.2333975,
    7.006125,
    16.20831,
    19.324417,
    15.819074,
    19.356344,
    17.93927,
    18.384487,
    18.001207,
    16.142382,
    21.02356,
    9.986794,
    6.614442,
    10.657583,
    6.6237283,
    8.433239,
    4.4907804,
    4.2819304,
    3.7269611,
    3.5132716,
    0.4662154,
    0.30799574,
    0.96793664,
    -0.23279454,
    -0.65458816,
    0.3362532,
    -0.25408295,
    0.06732974,
    0.4873681,
    0.51199776,
    0.14874719,
    -0.29994798,
    0.4666868,
    0.33490536,
    3.3489285,
    2.9599032,
    3.7671084,
    5.274986,
    11.143537,
    9.2554245,
    9.07235,
    9.138557,
    17.255503,
    18.355011,
    15.364281,
    17.336935,
    18.85955,
    17.050003,
    15.608138,
    15.812602,
    18.231024,
    11.6336155,
    6.9478188,
    11.149977,
    7.419574,
    10.250601,
    4.7022414,
    3.971905,
    4.7929826,
    3.3438401,
    -0.39000547,
    -0.28059074,
    0.6398243,
    0.54544014,
    0.6069346,
    -0.17257981,
    0.22857136,
    0.5565434,
    0.004583537,
    -1.6335539,
    -0.8888735,
    -0.51765877,
    0.25269827,
    -0.01876194,
    3.6656997,
    3.8518455,
    5.484056,
    6.189166,
    12.860901,
    9.803692,
    10.184517,
    8.937886,
    17.70772,
    18.956602,
    15.036017,
    18.585073,
    18.892986,
    18.184309,
    15.378883,
    13.1691475,
    16.713081,
    11.373385,
    10.050861,
    11.757488,
    10.44355,
    12.29941,
    4.694755,
    5.29064,
    3.8482742,
    3.204164,
    0.0923521,
    0.023937136,
    0.1471634,
    0.6328977,
    0.086753555,
    0.4752982,
    -0.6725007,
    0.39593527,
    0.22832835,
    -0.27118513,
    -0.8305444,
    0.61332023,
    -0.46385112,
    -0.07130288,
    3.392937,
    5.612763,
    5.2056,
    5.706025,
    15.220109,
    11.131699,
    11.811647,
    9.684384,
    18.768026,
    16.84839,
    13.052551,
    16.32535,
    17.554602,
    17.395172,
    14.127713,
    12.6871,
    17.62177,
    11.645812,
    8.629343,
    11.129438,
    11.581531,
    14.195255,
    4.8469067,
    5.1938415,
    4.0862703,
    3.181031,
    -1.0452468,
    -0.25019166,
    -0.7914238,
    0.12144237,
    -0.41462633,
    0.54280686,
    -0.69631076,
    0.3511648,
    0.004874259,
    -0.06835556,
    0.8735261,
    0.24838078,
    -0.31527227,
    0.52716863,
    3.9399889,
    6.0550613,
    6.129095,
    6.861085,
    18.186186,
    11.700109,
    9.944186,
    8.473949,
    16.194746,
    15.487744,
    11.69865,
    15.148699,
    17.62606,
    18.724825,
    14.773164,
    12.397501,
    17.29195,
    12.904611,
    10.236364,
    9.858109,
    12.551205,
    17.244278,
    5.081826,
    5.861555,
    4.532901,
    2.9011462,
    -0.6339103,
    -0.14527631,
    -0.34604034,
    0.16419859,
    -0.21205892,
    1.0102317,
    -0.6850754,
    -0.35831228,
    0.2243401,
    -0.12707797,
    0.12315286,
    0.75053287,
    -0.30611196,
    0.946708,
    3.2013948,
    5.563331,
    4.7585716,
    7.213843,
    20.686522,
    11.607341,
    12.30799,
    10.50174,
    15.599098,
    14.504682,
    13.629604,
    13.69594,
    17.019728,
    16.432478,
    13.931328,
    13.392891,
    16.40223,
    12.716988,
    10.136288,
    11.304484,
    14.544636,
    18.359613,
    5.5700507,
    5.302722,
    5.3971443,
    4.0632043,
    0.34419727,
    -0.43536162,
    0.2166448,
    -0.95898896,
    0.54851377,
    0.7104762,
    0.73580873,
    -0.025371978,
    -0.42447037,
    -0.055623855,
    -0.057257153,
    -0.042765763,
    -0.32910374,
    0.110769786,
    4.9113693,
    6.042119,
    5.789901,
    8.213889,
    21.399662,
    13.620898,
    12.268165,
    12.022924,
    15.812675,
    14.541431,
    11.235446,
    13.432023,
    16.380638,
    17.424328,
    13.075844,
    13.108509,
    16.125572,
    12.70376,
    9.833503,
    12.167731,
    15.966658,
    19.35662,
    4.726227,
    5.754112,
    5.277654,
    3.513394,
    0.27682012,
    -0.6424214,
    0.63972783,
    0.052361738,
    0.6900285,
    0.8120001,
    0.13217215,
    -0.06418637,
    -0.34938893,
    -0.1332957,
    -0.14414565,
    0.13367409,
    0.2113514,
    0.013457297,
    5.1611977,
    5.566288,
    5.6893077,
    6.982988,
    20.4595,
    14.453565,
    13.59946,
    10.934562,
    16.137613,
    14.927114,
    11.994792,
    13.434463,
    17.021969,
    17.274439,
    13.322607,
    11.919087,
    16.481926,
    12.076119,
    10.847066,
    11.398886,
    16.077639,
    19.727343,
    4.5308523,
    6.236413,
    4.8869467,
    3.9474933,
    0.5430834,
    -0.16916445,
    1.1437705,
    0.16070405,
    0.31188658,
    0.8880989,
    -0.14495048,
    -0.5266939,
    0.22656989,
    0.3505556,
    0.015732061,
    -0.005636345,
    -0.56870633,
    0.40287915,
    4.4800043,
    4.970619,
    4.5086727,
    7.2337227,
    21.180979,
    13.984755,
    12.418574,
    10.579776,
    14.925623,
    11.359912,
    10.660921,
    12.467203,
    17.208267,
    17.148045,
    11.586628,
    11.8577,
    13.493896,
    13.254265,
    10.851606,
    13.149869,
    17.053873,
    19.849815,
    4.9660897,
    5.8460274,
    3.998473,
    3.6802619,
    0.8031087,
    -0.013905935,
    0.3503995,
    0.31186494,
    -0.038673762,
    -0.07608058,
    0.21588215,
    -0.23191574,
    -0.3952367,
    -0.09744672,
    0.10716237,
    -1.3977432,
    -0.2775279,
    0.28267142,
    3.4341362,
    5.5165367,
    4.798283,
    5.5223513,
    23.267078,
    15.076336,
    13.030845,
    10.9562845,
    13.846566,
    11.140822,
    10.528686,
    12.319912,
    15.81127,
    17.356304,
    10.330765,
    10.917309,
    11.82135,
    11.22828,
    9.395469,
    12.859789,
    15.528548,
    18.173409,
    4.9549546,
    7.068773,
    5.830448,
    2.882567,
    -0.47524917,
    -0.3299339,
    0.19532575,
    -0.5605442,
    -0.05505767,
    -0.22165492,
    -0.4325593,
    0.13398468,
    -0.34254703,
    0.0140561955,
    -0.31874263,
    -0.14240773,
    -0.91078305,
    0.69452536,
    4.23155,
    5.7011547,
    6.0003905,
    6.377488,
    20.312622,
    13.978043,
    11.040157,
    11.176402,
    13.108543,
    9.652381,
    9.632209,
    11.781593,
    14.856762,
    15.745179,
    9.215103,
    9.966311,
    12.876652,
    11.37008,
    10.591258,
    10.1424675,
    14.367625,
    19.73172,
    3.84762,
    7.103483,
    3.7233605,
    2.376824,
    0.5252924,
    0.38380843,
    0.99321234,
    -0.46900645,
    0.12149067,
    0.42257598,
    0.0632253,
    -0.6670193,
    0.03464376,
    0.452787,
    0.29236665,
    -0.017891373,
    -0.075127214,
    0.9828477,
    2.3365817,
    5.2860856,
    4.3626456,
    5.785785,
    20.600492,
    12.966171,
    11.047343,
    9.063554,
    10.454045,
    10.47048,
    9.218836,
    11.104739,
    15.136548,
    14.689532,
    10.122101,
    9.4212675,
    11.134829,
    8.617753,
    9.327736,
    11.278048,
    13.085438,
    18.43459,
    3.9763334,
    5.9072723,
    3.9930198,
    3.4963682,
    0.2813723,
    1.0457343,
    0.31889322,
    0.37867522,
    1.2037315,
    -0.47904515,
    0.582204,
    0.68306595,
    -0.088313825,
    -0.107233785,
    -0.53984404,
    0.39104667,
    1.1425363,
    0.51777375,
    2.9267018,
    5.183814,
    4.495046,
    4.6087675,
    18.143732,
    12.06679,
    8.621597,
    7.8071413,
    9.6548195,
    8.168409,
    7.199488,
    7.962524,
    13.9421425,
    12.19501,
    8.027851,
    8.022394,
    8.449041,
    8.428407,
    7.2122917,
    9.045476,
    12.2283,
    16.851568,
    4.1475954,
    5.7582254,
    3.977257,
    1.8516432,
    -0.32922924,
    -0.12237206,
    -0.072756164,
    -0.6167613,
    0.5225413,
    0.37072095,
    -0.6287377,
    -0.7166235,
    -0.37311992,
    0.81874573,
    0.17337193,
    0.17729722,
    0.40824133,
    -0.3479744,
    2.9783738,
    4.5450144,
    3.9617758,
    4.9179983,
    15.7159395,
    10.0808935,
    7.922992,
    6.9472337,
    9.000638,
    7.62391,
    6.7539964,
    8.514194,
    12.004702,
    12.731859,
    7.173314,
    7.301387,
    7.240425,
    7.4015136,
    7.516923,
    8.6178665,
    9.913477,
    14.592376,
    4.5969114,
    5.9667635,
    2.2334886,
    2.1020658,
    -0.9194653,
    0.43381432,
    -0.74259335,
    -0.8438142,
    0.01724637,
    -0.6245163,
    0.34715256,
    -0.24820891,
    -0.6074153,
    -0.066010244,
    -0.05560958,
    -0.32758415,
    0.3784681,
    -0.09629097,
    2.7877793,
    4.203103,
    3.26329,
    4.44158,
    12.650619,
    8.000976,
    5.2695656,
    5.8276386,
    7.0067124,
    6.36843,
    5.256174,
    7.340733,
    9.230904,
    13.014863,
    5.453347,
    6.2923303,
    6.518343,
    6.5802903,
    5.615034,
    7.000242,
    8.82858,
    11.683347,
    3.8504424,
    4.365258,
    3.2354295,
    2.2202947,
    0.5615039,
    0.41533247,
    0.21722497,
    0.3176445,
    0.2709266,
    -0.2929376,
    0.090651914,
    -0.32017383,
    -0.30647907,
    0.15408067,
    -0.3604456,
    0.6241022,
    0.42943946,
    0.30790985,
    2.0098479,
    3.1669462,
    3.8518548,
    4.0607076,
    11.639872,
    5.7104745,
    7.125849,
    5.09103,
    5.6111135,
    3.951972,
    4.0356493,
    7.02897,
    11.430392,
    11.738871,
    4.115266,
    5.621048,
    5.3278913,
    5.120655,
    5.990115,
    5.7664003,
    5.7767644,
    9.013329,
    2.9515538,
    5.6055756,
    4.1827626,
    1.7799046,
    -0.21542077,
    0.24031225,
    -0.6824815,
    -0.6190339,
    0.6256524,
    -0.48574805,
    0.09997501,
    0.3266095,
    0.07135873,
    -0.3254111,
    -0.047491744,
    -0.014772129,
    -0.38849118,
    0.286563,
    2.9551277,
    3.957588,
    3.0914695,
    3.1707056,
    8.462824,
    4.728864,
    5.0381837,
    4.0804534,
    5.1110387,
    4.62399,
    4.415538,
    6.1308045,
    10.654469,
    10.723281,
    4.4972973,
    3.627521,
    3.8499038,
    4.373936,
    4.0010695,
    4.3314424,
    6.3237967,
    7.2798166,
    2.3315697,
    4.04032,
    3.2531312,
    2.022844,
    -0.5356632,
    0.52645034,
    0.11135009,
    -0.26490784,
    0.39241284,
    0.13336958,
    -0.15545088,
    -0.048340384,
    0.6705195,
    -0.14051451,
    -0.7617515,
    0.11379189,
    0.21909207,
    0.63809645,
    1.5451268,
    4.243852,
    3.2245193,
    3.3400161,
    6.511011,
    4.033045,
    2.8604522,
    3.6116364,
    3.5580635,
    3.1904101,
    2.9593391,
    4.813459,
    8.871713,
    8.875507,
    2.922824,
    2.6118903,
    3.5907378,
    2.6278322,
    3.5242443,
    3.0563798,
    4.969574,
    5.5496926,
    3.3797112,
    3.520721,
    2.3572729,
    1.7771024,
    -0.43368375,
    -0.6439688,
    -0.56648374,
    0.25869504,
    -0.13318418,
    -0.25542453,
    -1.2330167,
    0.34627095,
    1.5127228,
    -0.6055812,
    0.6232876,
    0.23605451,
    -0.5616809,
    0.500821,
]).reshape((40, 40))