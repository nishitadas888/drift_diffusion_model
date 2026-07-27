import pyddm
from pyddm import Model
from pyddm.models import DriftConstant, BoundConstant, NoiseConstant, ICPointSourceCenter, OverlayNonDecision

model = Model(
    drift=DriftConstant(drift=0.5),
    bound=BoundConstant(B=1),
    noise=NoiseConstant(noise=1),
    IC=ICPointSourceCenter(),
    overlay=OverlayNonDecision(nondectime=0.2),
    dx=0.01,
    dt=0.01,
    T_dur=2
)

sol = model.solve()
print("Model ran successfully!")
