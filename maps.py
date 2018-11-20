from selenium.common.exceptions import TimeoutException

from selene.api import *

config.timeout = 5
config.browser_name = 'chrome'
with open('commercial-addresses.tsv', encoding='utf8') as tsvfile:
    # f = open('test.tsv', "w+", encoding='utf8')
    lis = list(tsvfile)
    new = []
    for item in lis:
        a = item.split(' ')
        del a[-1]
        b = ' '.join(a)
        new.append(b)
    google_index = 0
    google_destination = 1
    print(len(new))
    origin = new[::2]
    destination = new[1::2]

    for _ in range(1):
        google_results = []
        f = open('test.tsv', "a", encoding='utf8')
        browser.open_url('https://www.google.com/maps/')
        s('#searchbox-directions').click()
        for _ in range(20):
            km = s(
                    '#section-directions-trip-0 > div:nth-child(2) > div:nth-child(1) '
                    '> div:nth-child(1) > div:nth-child(2) > div:nth-child(3)')
            metres = s(by.xpath('(//div[@class="section-directions-trip-numbers"])[1]/div[2]'))
            s('#sb_ifc51 > input:nth-child(1)').set('{}'.format(origin[google_index])).press_enter()
            s('#sb_ifc52 > input:nth-child(1)').set('{}'.format(destination[google_index])).press_enter()
            print(origin[google_index], 'index ' + str(google_index))
            print(destination[google_index], 'index ' + str(google_index))
            try:
                if metres.is_displayed():
                    print(metres.text)
                    google_distance = metres.text
                else:
                    print(km.text)
                    google_distance = km.text
            except TimeoutException:
                print("0 m")
                google_distance = "ERROR"
            f.write(origin[google_index] + " " + destination[google_index] + " " + google_distance + '\n')
            google_results.append(
                "Origin: {}, destination: {}, google maps distance {}, openstreetmaps distance".format(
                    origin[google_index], destination[google_index], google_distance))
            google_index += 1
        for i in google_results:
            print(i)
        f.close()
        browser.quit()
