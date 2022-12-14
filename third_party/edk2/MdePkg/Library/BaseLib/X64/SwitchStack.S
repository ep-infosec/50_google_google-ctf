#------------------------------------------------------------------------------
#
# Copyright (c) 2006 - 2018, Intel Corporation. All rights reserved.<BR>
# This program and the accompanying materials
# are licensed and made available under the terms and conditions of the BSD License
# which accompanies this distribution.  The full text of the license may be found at
# http://opensource.org/licenses/bsd-license.php.
#
# THE PROGRAM IS DISTRIBUTED UNDER THE BSD LICENSE ON AN "AS IS" BASIS,
# WITHOUT WARRANTIES OR REPRESENTATIONS OF ANY KIND, EITHER EXPRESS OR IMPLIED.
#
# Module Name:
#
#   SwitchStack.S
#
# Abstract:
#
#------------------------------------------------------------------------------


#------------------------------------------------------------------------------
# Routine Description:
#
#   Routine for switching stacks with 2 parameters
#
# Arguments:
#
#   (rcx) EntryPoint    - Entry point with new stack.
#   (rdx) Context1      - Parameter1 for entry point.
#   (r8)  Context2      - Parameter2 for entry point.
#   (r9)  NewStack      - The pointer to new stack.
#
# Returns:
#
#   None
#
#------------------------------------------------------------------------------
ASM_GLOBAL ASM_PFX(InternalSwitchStack)
ASM_PFX(InternalSwitchStack):
    pushq   %rbp
    movq    %rsp, %rbp

    mov     %rcx, %rax  // Shift registers for new call
    mov     %rdx, %rcx
    mov     %r8, %rdx
    #
    # Reserve space for register parameters (rcx, rdx, r8 & r9) on the stack,
    # in case the callee wishes to spill them.
    #
    lea     -0x20(%r9), %rsp
    pushq   $0        // stop gdb stack unwind
    jmp     *%rax     // call EntryPoint ()
