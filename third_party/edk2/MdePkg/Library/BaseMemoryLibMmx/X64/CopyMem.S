#
# ConvertAsm.py: Automatically generated from CopyMem.asm
#
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
#   CopyMem.S
#
# Abstract:
#
#   CopyMem function
#
# Notes:
#
#------------------------------------------------------------------------------


#------------------------------------------------------------------------------
#  VOID *
#  EFIAPI
#  InternalMemCopyMem (
#    IN VOID   *Destination,
#    IN VOID   *Source,
#    IN UINTN  Count
#    )
#------------------------------------------------------------------------------
ASM_GLOBAL ASM_PFX(InternalMemCopyMem)
ASM_PFX(InternalMemCopyMem):
    pushq   %rsi
    pushq   %rdi
    movq    %rdx, %rsi                  # rsi <- Source
    movq    %rcx, %rdi                  # rdi <- Destination
    leaq    -1(%rsi, %r8,), %r9         # r9 <- End of Source
    cmpq    %rdi, %rsi
    movq    %rdi, %rax                  # rax <- Destination as return value
    jae     L0
    cmpq    %rdi, %r9
    jae     L_CopyBackward              # Copy backward if overlapped
L0:
    movq    %r8, %rcx
    andq    $7, %r8
    shrq    $3, %rcx                    # rcx <- # of Qwords to copy
    jz      L_CopyBytes
    movd    %mm0, %r10                  # (Save mm0 in r10)
L1:
    movq    (%rsi), %mm0
    movntq  %mm0, (%rdi)
    addq    $8, %rsi
    addq    $8, %rdi
    loop    L1
    mfence
    movd    %r10, %mm0                  # (Restore mm0)
    jmp     L_CopyBytes
L_CopyBackward:
    movq    %r9, %rsi                   # rsi <- End of Source
    leaq    -1(%rdi, %r8,), %rdi        # rdi <- End of Destination
    std                                 # set direction flag
L_CopyBytes:
    movq    %r8, %rcx
    rep     movsb                       # Copy bytes backward
    cld
    popq    %rdi
    popq    %rsi
    ret
