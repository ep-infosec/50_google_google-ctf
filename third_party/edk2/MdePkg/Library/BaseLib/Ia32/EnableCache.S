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
#   EnableCache.S
#
# Abstract:
#
#   Flush all caches with a WBINVD instruction, clear the CD bit of CR0 to 0, and clear
#   the NW bit of CR0 to 0
#
# Notes:
#
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
# VOID
# EFIAPI
# AsmEnableCache (
#   VOID
#   );
#------------------------------------------------------------------------------
ASM_GLOBAL ASM_PFX(AsmEnableCache)
ASM_PFX(AsmEnableCache):
    wbinvd
    movl    %cr0, %eax
    btrl    $30, %eax
    btrl    $29, %eax
    movl    %eax, %cr0
    ret
