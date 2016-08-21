d = {'Adam': 95, 'Lisa': 85, 'Bart': 59}


def generate_tr(name, score):
    return '<tr><td>%s</td><td>%s</td></tr>' % (name, score)


tds = ['<tr><td>%s</td><td style="color:red">%s</td></tr>' %
       (name, score) for name, score in d.iteritems()]
print '<table border="1">'
print '<tr><th>Name</th><th>Score</th><tr>'
print '\n'.join(tds)
print '</table>'


def toUppers(L):
    return [x.upper() for x in L if isinstance(x, str)]


print toUppers(['Hello', 'world', 101])

