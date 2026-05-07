# -*- coding: utf-8 -*-
"""Running the test.
"""
import runpy
from matplotlib import pyplot as plt
from transp_exact import getsol

fig, axs = plt.subplots(
    1, 2, figsize=(10, 4)
)

# DIFFUSION

out = runpy.run_module(
    'transp_num', init_globals={'DIFF': 1.0, 'VELY': 0.0}
)

axs[0].plot(
    out['xax'], out['sol'], '-b'
)

ref = getsol(501, 0.0, 1.0, 0.01)

axs[0].plot(
    ref['x'][10::10], ref['u'][10::10], '.r'
)


# CONVECTION (+)

out = runpy.run_module(
    'transp_num', init_globals={'DIFF': 1.0, 'VELY': + 20.0}
)

axs[1].plot(
    out['xax'], out['sol'], '-b'
)

ref = getsol(501, 20.0, 1.0, 0.01)

axs[1].plot(
    ref['x'][10::10], ref['u'][10::10], '.r'
)

# CONVECTION (-)

out = runpy.run_module(
    'transp_num', init_globals={'DIFF': 1.0, 'VELY': - 20.0}
)

axs[1].plot(
    out['xax'], out['sol'], '-b'
)

ref = getsol(501, - 20.0, 1.0, 0.01)

axs[1].plot(
    ref['x'][10::10], ref['u'][10::10], '.r'
)

plt.tight_layout()
