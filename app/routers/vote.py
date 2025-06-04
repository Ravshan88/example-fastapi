from fastapi import Depends, HTTPException, status, Response, APIRouter
from sqlalchemy.orm import Session

from .. import models, schemas, database, oauth2

router = APIRouter(prefix="/vote", tags=["vote"])


@router.post("/", status_code=status.HTTP_201_CREATED)
def vote(vote: schemas.Vote, db: Session = Depends(database.get_db),
         current_user: int = Depends(oauth2.get_current_user)):
    post = db.query(models.Post).filter(models.Post.id == vote.post_id)
    if post.first() is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")
    vote_query = db.query(models.Vote).filter(models.Vote.post_id == vote.post_id,
                                              models.Vote.user_id == current_user.id)
    found_vote = vote_query.first()
    if vote.dir == 1:
        if found_vote:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Already voted")
        new_vote = models.Vote(post_id=vote.post_id, user_id=current_user.id)
        db.add(new_vote)
        db.commit()
        db.refresh(new_vote)
        return {"data": new_vote}
    if vote.dir == 0:
        if found_vote:
            vote_query.delete(synchronize_session=False)
            db.commit()
            return {"msg": "The vote was successfully deleted "}
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Vote not found")
