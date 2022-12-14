#------------------------------------------------------------------------------
#
# GetInterruptState() function for ARM
#
# Copyright (c) 2006 - 2018, Intel Corporation. All rights reserved.<BR>
# Portions copyright (c) 2008 - 2009, Apple Inc. All rights reserved.<BR>
# This program and the accompanying materials
# are licensed and made available under the terms and conditions of the BSD License
# which accompanies this distribution.  The full text of the license may be found at
# http://opensource.org/licenses/bsd-license.php.
#
# THE PROGRAM IS DISTRIBUTED UNDER THE BSD LICENSE ON AN "AS IS" BASIS,
# WITHOUT WARRANTIES OR REPRESENTATIONS OF ANY KIND, EITHER EXPRESS OR IMPLIED.
#
#------------------------------------------------------------------------------

.text
.p2align 2
GCC_ASM_EXPORT (GetInterruptState)

#/**
#  Retrieves the current CPU interrupt state.
#
#  Returns TRUE is interrupts are currently enabled. Otherwise
#  returns FALSE.
#
#  @retval TRUE  CPU interrupts are enabled.
#  @retval FALSE CPU interrupts are disabled.
#
#**/
#
#BOOLEAN
#EFIAPI
#GetInterruptState (
#  VOID
# );
#
ASM_PFX(GetInterruptState):
    mrs    R0, CPSR
    tst    R0, #0x80  @Check if IRQ is enabled.
    moveq  R0, #1
    movne  R0, #0
    bx     LR
