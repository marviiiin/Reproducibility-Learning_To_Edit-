from .counterfact import CounterFactDataset
from .zsre import ZsreDataset
try:
    from .coco_caption import CaptionDataset
except Exception:
    pass
try:
    from .vqa import VQADataset
except Exception:
    pass
from .wiki_recent import WikiRecentDataset
from .knowedit import KnowEditDataset
from .sanitization import SanitizationTrainDataset
from .multitask import MultiTaskDataset
from .personality import PersonalityDataset
from .safety import SafetyDataset
from .Cknowedit import CKnowEditDataset
from .MQuAKE import MQuAKEDataset
from .wikibigedit import WikiBigEditDataset
try:
    from .ComprehendEdit import ComprehendEditDataset
except Exception:
    pass
try:
    from .AKEW_both import AKEWUnifiedDataset
except Exception:
    pass
try:
    from .LEME import LongFormEditDataset
except Exception:
    pass