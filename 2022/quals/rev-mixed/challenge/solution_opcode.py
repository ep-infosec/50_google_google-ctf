# Copyright 2022 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
opcode module - potentially shared between dis and other modules which
operate on bytecodes (e.g. peephole optimizers).
"""

__all__ = ["cmp_op", "hasconst", "hasname", "hasjrel", "hasjabs",
           "haslocal", "hascompare", "hasfree", "opname", "opmap",
           "HAVE_ARGUMENT", "EXTENDED_ARG", "hasnargs"]

# It's a chicken-and-egg I'm afraid:
# We're imported before _opcode's made.
# With exception unheeded
# (stack_effect is not needed)
# Both our chickens and eggs are allayed.
#     --Larry Hastings, 2013/11/23

try:
    from _opcode import stack_effect
    __all__.append('stack_effect')
except ImportError:
    pass

cmp_op = ('<', '<=', '==', '!=', '>', '>=')

hasconst = []
hasname = []
hasjrel = []
hasjabs = []
haslocal = []
hascompare = []
hasfree = []
hasnargs = [] # unused

opmap = {}
opname = ['<%r>' % (op,) for op in range(256)]

_inline_cache_entries = [0] * 256

def def_op(name, op, entries=0):
    opname[op] = name
    opmap[name] = op
    _inline_cache_entries[op] = entries

def name_op(name, op, entries=0):
    def_op(name, op, entries)
    hasname.append(op)

def jrel_op(name, op, entries=0):
    def_op(name, op, entries)
    hasjrel.append(op)

def jabs_op(name, op, entries=0):
    def_op(name, op, entries)
    hasjabs.append(op)

# Instruction opcodes for compiled code
# Blank lines correspond to available opcodes

def_op('CACHE', 32) # YES
def_op('POP_TOP', 1)
def_op('PUSH_NULL', 2)
def_op("3???", 3)

def_op('NOP', 0)
def_op('UNARY_POSITIVE', 10)
def_op('UNARY_NEGATIVE', 11)
def_op('UNARY_NOT', 12)

def_op('UNARY_INVERT', 15)

def_op('BINARY_SUBSCR', 82, 4) # YES

def_op('GET_LEN', 30)
def_op('MATCH_MAPPING', 68)
def_op('MATCH_SEQUENCE', 9)
def_op('MATCH_KEYS', 33)

def_op('PUSH_EXC_INFO', 35)
def_op('CHECK_EXC_MATCH', 36)
def_op('CHECK_EG_MATCH', 37)

def_op('WITH_EXCEPT_START', 83)
def_op('GET_AITER', 50)
def_op('GET_ANEXT', 51)
def_op('BEFORE_ASYNC_WITH', 52)
def_op('BEFORE_WITH', 53)
def_op('END_ASYNC_FOR', 54)

def_op('STORE_SUBSCR', 60, 1)
def_op('DELETE_SUBSCR', 61)

def_op('GET_ITER', 31) # YES
def_op('GET_YIELD_FROM_ITER', 69)
def_op('PRINT_EXPR', 70)
def_op('LOAD_BUILD_CLASS', 71)

def_op('LOAD_ASSERTION_ERROR', 74)
def_op('RETURN_GENERATOR', 75)

def_op('LIST_TO_TUPLE', 25)
def_op('RETURN_VALUE', 49) # YES
def_op('IMPORT_STAR', 84)
def_op('SETUP_ANNOTATIONS', 85)
def_op('YIELD_VALUE', 86)
def_op('ASYNC_GEN_WRAP', 87)
def_op('PREP_RERAISE_STAR', 88)
def_op('POP_EXCEPT', 89)

HAVE_ARGUMENT = 90              # Opcodes from here have an argument:

name_op('STORE_NAME', 151) #YES      # Index in name list
name_op('DELETE_NAME', 91)      # ""
def_op('UNPACK_SEQUENCE', 143, 1)  # YES  # Number of tuple items
jrel_op('FOR_ITER', 182) # YES
def_op('UNPACK_EX', 110)
name_op('STORE_ATTR', 95, 4)       # Index in name list
name_op('DELETE_ATTR', 100)      # ""
name_op('STORE_GLOBAL', 90)     # ""
name_op('DELETE_GLOBAL', 124)    # ""
def_op('SWAP', 132)
def_op('LOAD_CONST', 96)       # YES
hasconst.append(96)
name_op('LOAD_NAME', 101)       # Index in name list
def_op('BUILD_TUPLE', 102)      # Number of tuple items
def_op('BUILD_LIST', 116) # YES       # Number of list items
def_op('BUILD_SET', 107)        # Number of set items
def_op('BUILD_MAP', 105)        # Number of dict entries
name_op('LOAD_ATTR', 188, 4) # YES      # Index in name list
def_op('COMPARE_OP', 104, 2) #YES?      # Comparison operator
hascompare.append(104)
name_op('IMPORT_NAME', 171) # YES     # Index in name list
name_op('IMPORT_FROM', 109)     # Index in name list
jrel_op('JUMP_FORWARD', 94) #YES    # Number of words to skip
jrel_op('JUMP_IF_FALSE_OR_POP', 111) # Number of words to skip
jrel_op('JUMP_IF_TRUE_OR_POP', 112)  # ""
jrel_op('POP_JUMP_FORWARD_IF_FALSE', 186) # YES
jrel_op('POP_JUMP_FORWARD_IF_TRUE', 115)
name_op('LOAD_GLOBAL', 185, 5) # YES    # Index in name list
name_op('LOAD_GLOBAL_BUILTIN', 27, 5) # YES    # Index in name list
def_op('IS_OP', 117)
def_op('CONTAINS_OP', 118)
def_op('RERAISE', 122)
def_op('COPY', 120)
def_op('BINARY_OP', 198, 1) # YES
jrel_op('SEND', 123) # Number of bytes to skip
def_op('LOAD_FAST', 98) # YES        # Local variable number
haslocal.append(98)
def_op('STORE_FAST', 141) #YES       # Local variable number
haslocal.append(141)
def_op('DELETE_FAST', 126)      # Local variable number
haslocal.append(126)
jrel_op('POP_JUMP_FORWARD_IF_NOT_NONE', 128)
jrel_op('POP_JUMP_FORWARD_IF_NONE', 129)
def_op('RAISE_VARARGS', 130)    # Number of raise arguments (1, 2, or 3)
def_op('GET_AWAITABLE', 131)
def_op('MAKE_FUNCTION', 99) # YES    # Flags
def_op('BUILD_SLICE', 133)      # Number of items
jrel_op('JUMP_BACKWARD_NO_INTERRUPT', 134) # Number of words to skip (backwards)
def_op('MAKE_CELL', 135)
hasfree.append(135)
def_op('LOAD_CLOSURE', 136)
hasfree.append(136)
def_op('LOAD_DEREF', 137)
hasfree.append(137)
def_op('STORE_DEREF', 138)
hasfree.append(138)
def_op('DELETE_DEREF', 139)
hasfree.append(139)
jrel_op('JUMP_BACKWARD', 123)    # Number of words to skip (backwards)

def_op('CALL_FUNCTION_EX', 108)  # Flags

def_op('EXTENDED_ARG', 144)
EXTENDED_ARG = 144
def_op('LIST_APPEND', 145)
def_op('SET_ADD', 160)
def_op('MAP_ADD', 147)
def_op('LOAD_CLASSDEREF', 148)
hasfree.append(148)
def_op('COPY_FREE_VARS', 149)

def_op('RESUME', 97) # YES
def_op('MATCH_CLASS', 152)

def_op('FORMAT_VALUE', 155)
def_op('BUILD_CONST_KEY_MAP', 156)
def_op('BUILD_STRING', 157)

name_op('LOAD_METHOD', 146, 10) # YES

def_op('LIST_EXTEND', 162)
def_op('SET_UPDATE', 163)
def_op('DICT_MERGE', 164)
def_op('DICT_UPDATE', 165)
def_op('PRECALL', 191, 1) # YES

def_op('CALL', 142, 4) # YES
def_op('KW_NAMES', 172)
hasconst.append(172)

jrel_op('POP_JUMP_BACKWARD_IF_NOT_NONE', 173)
jrel_op('POP_JUMP_BACKWARD_IF_NONE', 174)
jrel_op('POP_JUMP_BACKWARD_IF_FALSE', 175)
jrel_op('POP_JUMP_BACKWARD_IF_TRUE', 176)


del def_op, name_op, jrel_op, jabs_op

_nb_ops = [
    ("NB_ADD", "+"),
    ("NB_AND", "&"),
    ("NB_FLOOR_DIVIDE", "//"),
    ("NB_LSHIFT", "<<"),
    ("NB_MATRIX_MULTIPLY", "@"),
    ("NB_MULTIPLY", "*"),
    ("NB_REMAINDER", "%"),
    ("NB_OR", "|"),
    ("NB_POWER", "**"),
    ("NB_RSHIFT", ">>"),
    ("NB_SUBTRACT", "-"),
    ("NB_TRUE_DIVIDE", "/"),
    ("NB_XOR", "^"),
    ("NB_INPLACE_ADD", "+="),
    ("NB_INPLACE_AND", "&="),
    ("NB_INPLACE_FLOOR_DIVIDE", "//="),
    ("NB_INPLACE_LSHIFT", "<<="),
    ("NB_INPLACE_MATRIX_MULTIPLY", "@="),
    ("NB_INPLACE_MULTIPLY", "*="),
    ("NB_INPLACE_REMAINDER", "%="),
    ("NB_INPLACE_OR", "|="),
    ("NB_INPLACE_POWER", "**="),
    ("NB_INPLACE_RSHIFT", ">>="),
    ("NB_INPLACE_SUBTRACT", "-="),
    ("NB_INPLACE_TRUE_DIVIDE", "/="),
    ("NB_INPLACE_XOR", "^="),
]

_specializations = {
    "BINARY_OP": [
        "BINARY_OP_ADAPTIVE",
        "BINARY_OP_ADD_FLOAT",
        "BINARY_OP_ADD_INT",
        "BINARY_OP_ADD_UNICODE",
        "BINARY_OP_INPLACE_ADD_UNICODE",
        "BINARY_OP_MULTIPLY_FLOAT",
        "BINARY_OP_MULTIPLY_INT",
        "BINARY_OP_SUBTRACT_FLOAT",
        "BINARY_OP_SUBTRACT_INT",
    ],
    "BINARY_SUBSCR": [
        "BINARY_SUBSCR_ADAPTIVE",
        "BINARY_SUBSCR_DICT",
        "BINARY_SUBSCR_GETITEM",
        "BINARY_SUBSCR_LIST_INT",
        "BINARY_SUBSCR_TUPLE_INT",
    ],
    "CALL": [
        "CALL_ADAPTIVE",
        "CALL_PY_EXACT_ARGS",
        "CALL_PY_WITH_DEFAULTS",
    ],
    "COMPARE_OP": [
        "COMPARE_OP_ADAPTIVE",
        "COMPARE_OP_FLOAT_JUMP",
        "COMPARE_OP_INT_JUMP",
        "COMPARE_OP_STR_JUMP",
    ],
    "EXTENDED_ARG": [
        "EXTENDED_ARG_QUICK",
    ],
    "JUMP_BACKWARD": [
        "JUMP_BACKWARD_QUICK",
    ],
    "LOAD_ATTR": [
        "LOAD_ATTR_ADAPTIVE",
        "LOAD_ATTR_INSTANCE_VALUE",
        "LOAD_ATTR_MODULE",
        "LOAD_ATTR_SLOT",
        "LOAD_ATTR_WITH_HINT",
    ],
    "LOAD_CONST": [
        "LOAD_CONST__LOAD_FAST",
    ],
    "LOAD_FAST": [
        "LOAD_FAST__LOAD_CONST",
        "LOAD_FAST__LOAD_FAST",
    ],
    "LOAD_GLOBAL": [
        "LOAD_GLOBAL_ADAPTIVE",
        "LOAD_GLOBAL_BUILTIN",
        "LOAD_GLOBAL_MODULE",
    ],
    "LOAD_METHOD": [
        "LOAD_METHOD_ADAPTIVE",
        "LOAD_METHOD_CLASS",
        "LOAD_METHOD_MODULE",
        "LOAD_METHOD_NO_DICT",
        "LOAD_METHOD_WITH_DICT",
        "LOAD_METHOD_WITH_VALUES",
    ],
    "PRECALL": [
        "PRECALL_ADAPTIVE",
        "PRECALL_BOUND_METHOD",
        "PRECALL_BUILTIN_CLASS",
        "PRECALL_BUILTIN_FAST_WITH_KEYWORDS",
        "PRECALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS",
        "PRECALL_NO_KW_BUILTIN_FAST",
        "PRECALL_NO_KW_BUILTIN_O",
        "PRECALL_NO_KW_ISINSTANCE",
        "PRECALL_NO_KW_LEN",
        "PRECALL_NO_KW_LIST_APPEND",
        "PRECALL_NO_KW_METHOD_DESCRIPTOR_FAST",
        "PRECALL_NO_KW_METHOD_DESCRIPTOR_NOARGS",
        "PRECALL_NO_KW_METHOD_DESCRIPTOR_O",
        "PRECALL_NO_KW_STR_1",
        "PRECALL_NO_KW_TUPLE_1",
        "PRECALL_NO_KW_TYPE_1",
        "PRECALL_PYFUNC",
    ],
    "RESUME": [
        "RESUME_QUICK",
    ],
    "STORE_ATTR": [
        "STORE_ATTR_ADAPTIVE",
        "STORE_ATTR_INSTANCE_VALUE",
        "STORE_ATTR_SLOT",
        "STORE_ATTR_WITH_HINT",
    ],
    "STORE_FAST": [
        "STORE_FAST__LOAD_FAST",
        "STORE_FAST__STORE_FAST",
    ],
    "STORE_SUBSCR": [
        "STORE_SUBSCR_ADAPTIVE",
        "STORE_SUBSCR_DICT",
        "STORE_SUBSCR_LIST_INT",
    ],
    "UNPACK_SEQUENCE": [
        "UNPACK_SEQUENCE_ADAPTIVE",
        "UNPACK_SEQUENCE_LIST",
        "UNPACK_SEQUENCE_TUPLE",
        "UNPACK_SEQUENCE_TWO_TUPLE",
    ],
}
_specialized_instructions = [
    opcode for family in _specializations.values() for opcode in family
]
_specialization_stats = [
    "success",
    "failure",
    "hit",
    "deferred",
    "miss",
    "deopt",
]
