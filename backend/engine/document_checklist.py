from typing import List, Dict, Set
from backend.models.schemas import SchemeMatch, ConsolidatedDocuments

UNIVERSAL_DOC_PATTERNS = [
    "aadhaar",
    "pan card",
    "bank account",
    "bank statement",
    "bank passbook",
    "photograph",
    "photo",
    "identity proof",
    "residence proof",
    "voter",
    "income certificate",
    "caste certificate",
]


class DocumentChecklistManager:
    @staticmethod
    def generate_consolidated_checklist(
        direct_matches: List[SchemeMatch], near_miss_matches: List[SchemeMatch]
    ) -> ConsolidatedDocuments:
        """
        Consolidates and groups required documents across matched schemes.
        """
        all_schemes = [m.scheme for m in direct_matches] + [m.scheme for m in near_miss_matches]
        
        universal_docs: Set[str] = set()
        scheme_specific_docs: Dict[str, List[str]] = {}
        all_seen_docs: Set[str] = set()

        for scheme in all_schemes:
            specific_for_this: List[str] = []
            for doc in scheme.required_documents:
                doc_clean = doc.strip()
                all_seen_docs.add(doc_clean)
                doc_lower = doc_clean.lower()

                # Check if it matches a common universal document pattern
                is_universal = any(pattern in doc_lower for pattern in UNIVERSAL_DOC_PATTERNS)
                if is_universal:
                    universal_docs.add(doc_clean)
                else:
                    specific_for_this.append(doc_clean)

            if specific_for_this:
                scheme_specific_docs[scheme.name] = specific_for_this

        # Sort for clean presentation
        sorted_universal = sorted(list(universal_docs))

        return ConsolidatedDocuments(
            universal_documents=sorted_universal,
            scheme_specific_documents=scheme_specific_docs,
            total_unique_documents=len(all_seen_docs),
        )
