; Copyright 2022 Google LLC
;
; Licensed under the Apache License, Version 2.0 (the "License");
; you may not use this file except in compliance with the License.
; You may obtain a copy of the License at
;
;     https://www.apache.org/licenses/LICENSE-2.0
;
; Unless required by applicable law or agreed to in writing, software
; distributed under the License is distributed on an "AS IS" BASIS,
; WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
; See the License for the specific language governing permissions and
; limitations under the License.
;
; Compilation: as31 -Fbyte shellcode.a51
; This will generate shellcode.a51.byte file.
;
.org 0xa80
  nop
  nop
  nop
  nop
  nop
  nop
  nop
  nop

  clr a
  mov r0, a

loop:
  mov a, r0
  mov 0xee, a
  mov a, 0xef
  mov 0xf2, a
  inc r0

  mov a, r0
  cpl a
  jnz loop

  mov 0xff, a


