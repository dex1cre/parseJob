import config
import parse

def write_to_file(data):
    before = """
    <!doctype html>
    <html>
      <head>
          <meta charset="utf-8">
              <title>micro-time</title>
                  <link href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">
                      <style>
                      form {
                            margin: 0 auto;
                            min-width: 200px;
                            width: 500px;
                      }

                      .jobs {
                            margin-top: 20px;
                      }

                      .jobs > li {
                            display: block;
                      }

                      .tags > li {
                            display: inline-block;
                            margin-left: 5px;
                      }

                      .tags > li:first-child {
                            margin-left: 0;
                      }
                          </style>
                            </head>
                            <body>
                              <div class="container">
                                  <div class="row">
                                        <div class="col-md-6 col-sm-6 col-xs-12">
                                                <form method="get" action="/" class="center">
                                                          <h3>Поиск по заданию</h3>
                                                                    <div class="form-group">
                                                                                <input type="text" name="input_text" id="input_text" class="form-control" placeholder="Предлагаю вам сюда что-нибудь написать" required>
                                                                                          </div>
                                                                                                    <button class="btn">Найти</button>
                                                                                                            </form>

                                                                                                                    <ul class="jobs">
    """

    after = """
    </ul>
          </div>
              </div>
                </div>
                </body>
    """
    midle = ""
    print("\nStart writing to file...")
    for i in data:
        midle = midle + '<li><h4>' + i[0] + '</h4><ul class="tags">'
        for j in i[2]:
            midle = midle + '<li>' + j + '</li>'
        midle = midle + '</ul><p class="description">' + i[1] + '</p>'
        midle = midle + '<a href="' + config.url + i[3] + '" class="btn btn-primary">'
        midle = midle + 'Перейти к заказу</a></li><hr />'

    html = before + midle + after
    file = open("index.html", "w")
    file.write(html)
    file.close()

    return html

def main():
   print(write_to_file(parse.parse(parse.get_html(config.url))))

if __name__ == "__main__":
    main()
