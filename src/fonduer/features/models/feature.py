from sqlalchemy import Column, Float
from sqlalchemy.dialects import postgresql

from fonduer.meta import Meta
from fonduer.utils.models.annotation import AnnotationKeyMixin, AnnotationMixin

_meta = Meta.init()


class FeatureKey(AnnotationKeyMixin, _meta.Base):
    pass


class Feature(AnnotationMixin, _meta.Base):
    """
    An element of a representation of a Candidate in a feature space.

    A Feature's annotation key identifies the definition of the Feature, e.g.,
    a function that implements it or the library name and feature name in an
    automatic featurization library.
    """

    values = Column(postgresql.ARRAY(Float), nullable=False)
