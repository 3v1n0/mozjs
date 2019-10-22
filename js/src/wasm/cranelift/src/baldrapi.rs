/* Copyright 2018 Mozilla Foundation
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

//! This module exports the bindings generated by bindgen form the baldrapi.h file.
//!
//! The Baldr API consists of a set of C functions and some associated types.

#![allow(non_upper_case_globals)]
#![allow(non_camel_case_types)]
#![allow(non_snake_case)]
// We need to allow dead code because the Rustc compiler complains about variants never being
// constructed in TypeCode, which is true because these values come from C++.
#![allow(dead_code)]

use cranelift_codegen::binemit::CodeOffset;
use cranelift_codegen::entity::EntityRef;
use cranelift_codegen::ir::SourceLoc;
use cranelift_wasm::FuncIndex;

use compile::CompiledFunc;

include!(concat!(env!("OUT_DIR"), "/bindings.rs"));

impl CraneliftFuncCompileInput {
    pub fn bytecode(&self) -> &[u8] {
        use std::slice;
        unsafe { slice::from_raw_parts(self.bytecode, self.bytecodeSize) }
    }
}

impl CraneliftCompiledFunc {
    pub fn reset(&mut self, compiled_func: &CompiledFunc) {
        self.numMetadata = compiled_func.metadata.len();
        self.metadatas = compiled_func.metadata.as_ptr();

        self.framePushed = compiled_func.frame_pushed as usize;
        self.containsCalls = compiled_func.contains_calls;

        self.code = compiled_func.code_buffer.as_ptr();
        self.codeSize = compiled_func.code_buffer.len();
    }
}

impl CraneliftMetadataEntry {
    pub fn direct_call(code_offset: CodeOffset, func_index: FuncIndex, srcloc: SourceLoc) -> Self {
        Self {
            which: CraneliftMetadataEntry_Which_DirectCall,
            codeOffset: code_offset,
            moduleBytecodeOffset: srcloc.bits(),
            extra: func_index.index(),
        }
    }

    pub fn indirect_call(code_offset: CodeOffset, srcloc: SourceLoc) -> Self {
        Self {
            which: CraneliftMetadataEntry_Which_IndirectCall,
            codeOffset: code_offset,
            moduleBytecodeOffset: srcloc.bits(),
            extra: 0,
        }
    }

    pub fn trap(code_offset: CodeOffset, srcloc: SourceLoc, which: Trap) -> Self {
        Self {
            which: CraneliftMetadataEntry_Which_Trap,
            codeOffset: code_offset,
            moduleBytecodeOffset: srcloc.bits(),
            extra: which as usize,
        }
    }

    pub fn memory_access(code_offset: CodeOffset, srcloc: SourceLoc) -> Self {
        Self {
            which: CraneliftMetadataEntry_Which_MemoryAccess,
            codeOffset: code_offset,
            moduleBytecodeOffset: srcloc.bits(),
            extra: 0,
        }
    }

    pub fn symbolic_access(code_offset: CodeOffset, sym: BD_SymbolicAddress) -> Self {
        Self {
            which: CraneliftMetadataEntry_Which_SymbolicAccess,
            codeOffset: code_offset,
            moduleBytecodeOffset: 0,
            extra: sym as usize,
        }
    }
}
