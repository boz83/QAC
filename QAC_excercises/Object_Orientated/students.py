class student():
  def __init__(self, id, forename, surname, course, email, password):
    self.id = id
    self.forename = forename
    self.surname = surname
    self.course = course
    self.email = email
    self.password = password


Steven = student("1", "Steven", "Bore", "Web Application Development", "smtbore@gmail.com", "JavascriptBetterThanPython")
  
print(getattr(Steven, "email"))