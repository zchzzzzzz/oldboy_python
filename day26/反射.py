class room:
      id=123
      def __init__(self,name):
       self.name=name
      def __getattr__(self):
       print("getattr:")
      def __delattr__(self):
          print("delattr")
room1=room("中南海")
del room1.name
