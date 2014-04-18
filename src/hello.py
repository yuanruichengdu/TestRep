#!python
#encoding:utf-8

def hello(name='world'):
    return 'hello %(name)s' % dict(name=name)

if __name__=="__main__":
    print(hello())
