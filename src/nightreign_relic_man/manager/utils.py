from dataclasses import dataclass

@dataclass
class TextZone:
    """Helper class to handle selecting rectangles in PIL.Image screenshots.
    Logic handles screenshot taken from different resolutions."""
    left_rel: int
    top_rel: int
    w_rel: int
    h_rel: int
    im_w: int
    im_h: int

    def pil_crop(self):
        right_rel = self.left_rel + self.w_rel
        bottom_rel = self.top_rel + self.h_rel
        return (
            int(self.im_w * self.left_rel), int(self.im_h * self.top_rel),
            int(self.im_w * right_rel), int(self.im_h * bottom_rel)
        )
