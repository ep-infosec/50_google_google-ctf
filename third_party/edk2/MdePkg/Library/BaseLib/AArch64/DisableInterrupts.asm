;------------------------------------------------------------------------------
;
; DisableInterrupts() for AArch64
;
; Copyright (c) 2006 - 2009, Intel Corporation. All rights reserved.<BR>
; Portions copyright (c) 2008 - 2009, Apple Inc. All rights reserved.<BR>
; Portions copyright (c) 2011 - 2013, ARM Ltd. All rights reserved.<BR>
; This program and the accompanying materials
; are licensed and made available under the terms and conditions of the BSD License
; which accompanies this distribution.  The full text of the license may be found at
; http://opensource.org/licenses/bsd-license.php.
;
; THE PROGRAM IS DISTRIBUTED UNDER THE BSD LICENSE ON AN "AS IS" BASIS,
; WITHOUT WARRANTIES OR REPRESENTATIONS OF ANY KIND, EITHER EXPRESS OR IMPLIED.
;
;------------------------------------------------------------------------------

  EXPORT DisableInterrupts
  AREA BaseLib_LowLevel, CODE, READONLY

DAIF_WR_IRQ_BIT     EQU     (1 << 1)

;/**
;  Disables CPU interrupts.
;
;**/
;VOID
;EFIAPI
;DisableInterrupts (
;  VOID
;  );
;
DisableInterrupts
    msr  daifset, #DAIF_WR_IRQ_BIT
    ret

  END
