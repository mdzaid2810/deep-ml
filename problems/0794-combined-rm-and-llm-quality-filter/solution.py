import numpy as np
def combined_quality_filter(rm_scores, llm_scores):
    """
    Return a boolean list marking high-quality samples by combined RM and LLM criteria.
    """
    if len(rm_scores)==0:
        return []

    rm_threshold = np.percentile(rm_scores,75)
    llm_max = np.max(llm_scores)

    result=[]

    for rm,llm in zip(rm_scores,llm_scores):
        keep = (rm >= rm_threshold) or (llm == llm_max)
        result.append(bool(keep))

    return result