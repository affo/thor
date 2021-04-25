
class ThorException(Exception):
    pass


class VisitorException(ThorException):
    def __init__(self, ctx, msg, *fmtargs):
        prefix = "line " + str(ctx.start.line) + ":" + str(ctx.start.column) + " "
        msg = prefix + msg.format(*fmtargs)
        super().__init__(msg)


class ParseException(ThorException):
    pass
