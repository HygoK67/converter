from collections import Counter
from typing import List, Optional

from marker.schema.bbox import BboxElement
from marker.schema.schema import Block, Span
from surya.schema import TextDetectionResult, LayoutResult


class Page(BboxElement):
    blocks: List[Block]
    pnum: int
    column_count: Optional[int] = None
    rotation: Optional[int] = None # Rotation degrees of the page
    text_lines: Optional[TextDetectionResult] = None
    layout: Optional[LayoutResult] = None

    def get_nonblank_lines(self):
        lines = self.get_all_lines()
        nonblank_lines = [l for l in lines if l.prelim_text.strip()]
        return nonblank_lines

    def get_all_lines(self):
        lines = [l for b in self.blocks for l in b.lines]
        return lines

    def get_nonblank_spans(self) -> List[Span]:
        lines = [l for b in self.blocks for l in b.lines]
        spans = [s for l in lines for s in l.spans if s.text.strip()]
        return spans

    def get_font_stats(self):
        fonts = [s.font for s in self.get_nonblank_spans()]
        font_counts = Counter(fonts)
        return font_counts

    def get_line_height_stats(self):
        heights = [l.bbox[3] - l.bbox[1] for l in self.get_nonblank_lines()]
        height_counts = Counter(heights)
        return height_counts

    def get_line_start_stats(self):
        starts = [l.bbox[0] for l in self.get_nonblank_lines()]
        start_counts = Counter(starts)
        return start_counts

    def get_min_line_start(self):
        starts = [l.bbox[0] for l in self.get_nonblank_lines() if l.spans[0].block_type == "Text"]
        if len(starts) == 0:
            raise IndexError("No lines found")
        return min(starts)

    @property
    def prelim_text(self):
        return "\n".join([b.prelim_text for b in self.blocks])
