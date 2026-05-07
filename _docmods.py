# -*- coding: utf-8 -*-
"""Documentation maker — modules.
"""
import docspyer
import femone

DOCPATH = 'docs/sources'

MODULES = [
    femone.fem, femone.mesh
]

config = {
    'docsname': 'femone',
    'hostname': 'femone',
    'modrefs': True,
    'clsverbs': 2
}

docspyer.docmods(
    MODULES, DOCPATH, **config
)
