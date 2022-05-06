from flask import Flask, request, render_template
import json
import random

app = Flask(__name__)

@app.route('/')
def displaySearchSelect():
    print('display index')

    return render_template('search_select.html')

@app.route('/', methods=['POST'])
def onButtonPush():
    print('button pushed')

    if request.form.get('select_home_search'):
        print('select home search')
        return render_template('home_search.html', searchResults = [])
    elif request.form.get('select_job_search'):
        print('select job search')
        return render_template('job_search.html', searchResults = [])
    elif request.form.get('back'):
        print('back')
        return render_template('search_select.html')
    elif request.form.get('search_homes'):
        print('search homes')
        location = request.form.get('location')
        priceLower = int(request.form.get('priceLower'))
        priceUpper = int(request.form.get('priceUpper'))
        searchType = request.form.get('searchType')
        searchResults = []
        if priceLower <= priceUpper:
            types = ['Apartment', 'Townhouse', 'House']
            for i in range(random.randint(5, 10)):
                result = {}
                result['name'] = 'Home Name ' + str(i) + ' (' + location + ')'
                if searchType == 'any':
                    result['type'] = types[random.randint(0, 2)]
                else:
                    result['type'] = searchType
                result['price'] = random.randint(priceLower, priceUpper)
                result['contactNum'] = random.randint(100000000, 999999999)
                searchResults.append(result)
        else:
            print('invalid price range')
        return render_template('home_search.html', searchResults = searchResults)
    elif request.form.get('search_jobs'):
        print('search jobs')
        occupation = request.form.get('occupation')
        location = request.form.get('location')
        salaryLower = int(request.form.get('salaryLower'))
        salaryUpper = int(request.form.get('salaryUpper'))
        searchResults = []
        if salaryLower <= salaryUpper:
            for i in range(random.randint(5, 10)):
                result = {}
                result['name'] = 'Job Name ' + str(i) + ' (' + occupation + ')'
                result['salary'] = random.randint(salaryLower, salaryUpper)
                result['contactNum'] = random.randint(100000000, 999999999)
                searchResults.append(result)
        else:
            print('invalid salary range')
        return render_template('job_search.html', searchResults = searchResults)
    else:
        print('could not determine button press')
        return ''

# main function
def main():
    print('hello world')

if __name__ == '__main__':
    main()
