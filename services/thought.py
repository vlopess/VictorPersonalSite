from repository.thoughtRepository import thoughtRepository


class ThougthController:
  def getThought():
    try:
      t = thoughtRepository()
      thoughts = t.select()
      return thoughts
    except Exception as exception:
      raise
    

  def addThought(t):
    try:
      tt = thoughtRepository()
      tt.insert(t)
    except Exception as exception:
      raise
