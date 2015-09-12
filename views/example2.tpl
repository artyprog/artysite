<%!
  
    import re

    def filter(text):
        return re.sub(r'@', '', text)
%>




Filter "a@t" : ${filter('xxxxxxxxxxxxx@txxxxx')}

