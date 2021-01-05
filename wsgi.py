from app.main import app

if __name__ == "__main__":
  app.run(debug=True) 

from wsgi_basic_auth import BasicAuth
application = BasicAuth(application)
