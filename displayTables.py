def viewTable(headings,data):
    for heads in headings:
        print("%25s" % heads,end="\t")
    print()
    for rows in data:
        for cols in rows:
            print("%25s" % cols,end="\t")
        print()
