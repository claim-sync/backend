from sqlalchemy import Column, Integer, String, DateTime, Boolean, Text, ForeignKey, Float, JSON
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.db.base_class import Base

class FactCheck(Base):
    __tablename__ = "fact_checks"
    
    id = Column(Integer, primary_key=True, index=True)
    upload_id = Column(Integer, ForeignKey("uploads.id"))
    
    # Analysis results
    trust_score = Column(Float)  # 0.0 to 1.0
    confidence = Column(Float)   # 0.0 to 1.0
    verdict = Column(String)     # true, false, mixed, unverified
    
    # Extracted claims
    claims = Column(JSON)  # List of extracted claims
    sources = Column(JSON)  # Verification sources
    explanations = Column(JSON)  # Detailed explanations
    
    # Flags
    is_deepfake = Column(Boolean, default=False)
    is_manipulated = Column(Boolean, default=False)
    has_misinformation = Column(Boolean, default=False)
    
    # Processing details
    processing_time = Column(Float)  # seconds
    model_versions = Column(JSON)    # AI model versions used
    
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    # Relationships
    upload = relationship("Upload", back_populates="fact_checks")