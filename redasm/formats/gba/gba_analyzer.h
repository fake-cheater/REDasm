#ifndef GBA_ANALYZER_H
#define GBA_ANALYZER_H

#include "../../analyzer/analyzer.h"

namespace REDasm {

class GbaAnalyzer : public Analyzer
{
    public:
        GbaAnalyzer(DisassemblerAPI* disassembler, const SignatureFiles& signaturefiles);
        virtual void analyze(InstructionsPool &listing);

    private:
        void renameEPBranch(InstructionsPool &listing, SymbolTable *symboltable);
};

} // namespace REDasm

#endif // GBA_ANALYZER_H
