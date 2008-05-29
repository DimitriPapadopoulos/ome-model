#!/usr/bin/env python

#
# Generated Mon May 26 14:04:33 2008 by generateDS.py.
#

import sys
import getopt
from xml.dom import minidom
from xml.dom import Node

#
# If you have installed IPython you can uncomment and use the following.
# IPython is available from http://ipython.scipy.org/.
#

## from IPython.Shell import IPShellEmbed
## args = ''
## ipshell = IPShellEmbed(args,
##     banner = 'Dropping into IPython',
##     exit_msg = 'Leaving Interpreter, back to program.')

# Then use the following line where and when you want to drop into the
# IPython shell:
#    ipshell('<some message> -- Entering ipshell.\nHit Ctrl-D to exit')

#
# Support/utility functions.
#

def showIndent(outfile, level):
    for idx in range(level):
        outfile.write('    ')

def quote_xml(inStr):
    s1 = (isinstance(inStr, basestring) and inStr or
          '%s' % inStr)
    s1 = s1.replace('&', '&amp;')
    s1 = s1.replace('<', '&lt;')
    s1 = s1.replace('>', '&gt;')
    return s1

def quote_attrib(inStr):
    s1 = (isinstance(inStr, basestring) and inStr or
          '%s' % inStr)
    s1 = s1.replace('&', '&amp;')
    s1 = s1.replace('"', '&quot;')
    s1 = s1.replace('<', '&lt;')
    s1 = s1.replace('>', '&gt;')
    return s1

def quote_python(inStr):
    s1 = inStr
    if s1.find("'") == -1:
        if s1.find('\n') == -1:
            return "'%s'" % s1
        else:
            return "'''%s'''" % s1
    else:
        if s1.find('"') != -1:
            s1 = s1.replace('"', '\\"')
        if s1.find('\n') == -1:
            return '"%s"' % s1
        else:
            return '"""%s"""' % s1


class MixedContainer:
    # Constants for category:
    CategoryNone = 0
    CategoryText = 1
    CategorySimple = 2
    CategoryComplex = 3
    # Constants for content_type:
    TypeNone = 0
    TypeText = 1
    TypeString = 2
    TypeInteger = 3
    TypeFloat = 4
    TypeDecimal = 5
    TypeDouble = 6
    TypeBoolean = 7
    def __init__(self, category, content_type, name, value):
        self.category = category
        self.content_type = content_type
        self.name = name
        self.value = value
    def getCategory(self):
        return self.category
    def getContenttype(self, content_type):
        return self.content_type
    def getValue(self):
        return self.value
    def getName(self):
        return self.name
    def export(self, outfile, level, name):
        if self.category == MixedContainer.CategoryText:
            outfile.write(self.value)
        elif self.category == MixedContainer.CategorySimple:
            self.exportSimple(outfile, level, name)
        else:    # category == MixedContainer.CategoryComplex
            self.value.export(outfile, level, name)
    def exportSimple(self, outfile, level, name):
        if self.content_type == MixedContainer.TypeString:
            outfile.write('<%s>%s</%s>' % (self.name, self.value, self.name))
        elif self.content_type == MixedContainer.TypeInteger or \
                self.content_type == MixedContainer.TypeBoolean:
            outfile.write('<%s>%d</%s>' % (self.name, self.value, self.name))
        elif self.content_type == MixedContainer.TypeFloat or \
                self.content_type == MixedContainer.TypeDecimal:
            outfile.write('<%s>%f</%s>' % (self.name, self.value, self.name))
        elif self.content_type == MixedContainer.TypeDouble:
            outfile.write('<%s>%g</%s>' % (self.name, self.value, self.name))
    def exportLiteral(self, outfile, level, name):
        if self.category == MixedContainer.CategoryText:
            showIndent(outfile, level)
            outfile.write('MixedContainer(%d, %d, "%s", "%s"),\n' % \
                (self.category, self.content_type, self.name, self.value))
        elif self.category == MixedContainer.CategorySimple:
            showIndent(outfile, level)
            outfile.write('MixedContainer(%d, %d, "%s", "%s"),\n' % \
                (self.category, self.content_type, self.name, self.value))
        else:    # category == MixedContainer.CategoryComplex
            showIndent(outfile, level)
            outfile.write('MixedContainer(%d, %d, "%s",\n' % \
                (self.category, self.content_type, self.name,))
            self.value.exportLiteral(outfile, level + 1)
            showIndent(outfile, level)
            outfile.write(')\n')


class _MemberSpec(object):
    def __init__(self, name='', data_type='', container=0):
        self.name = name
        self.data_type = data_type
        self.container = container
    def set_name(self, name): self.name = name
    def get_name(self): return self.name
    def set_data_type(self, data_type): self.data_type = data_type
    def get_data_type(self): return self.data_type
    def set_container(self, container): self.container = container
    def get_container(self): return self.container


#
# Data representation classes.
#

class people:
    _member_data_items = [
        _MemberSpec('person', 'person', 1),
        ]
    subclass = None
    superclass = None
    def __init__(self, person=None):
        if person is None:
            self.person = []
        else:
            self.person = person
    def factory(*args_, **kwargs_):
        if people.subclass:
            return people.subclass(*args_, **kwargs_)
        else:
            return people(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_person(self): return self.person
    def set_person(self, person): self.person = person
    def add_person(self, value): self.person.append(value)
    def insert_person(self, index, value): self.person[index] = value
    def export(self, outfile, level, name_='people', namespace_=''):
        showIndent(outfile, level)
        outfile.write('<%s%s>\n' % (namespace_, name_))
        self.exportChildren(outfile, level + 1, name_, namespace_)
        showIndent(outfile, level)
        outfile.write('</%s%s>\n' % (namespace_, name_))
    def exportAttributes(self, outfile, level, name_='people', namespace_=''):
        pass
    def exportChildren(self, outfile, level, name_='people', namespace_=''):
        for person_ in self.get_person():
            person_.export(outfile, level)
    def exportLiteral(self, outfile, level, name_='people'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('person=[\n')
        level += 1
        for person in self.person:
            showIndent(outfile, level)
            outfile.write('person(\n')
            person.exportLiteral(outfile, level)
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        pass
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'person':
            obj_ = person.factory()
            obj_.build(child_)
            self.person.append(obj_)
    def walk_and_update(self):
        members = people._member_data_items
        for member in members:
            obj1 = getattr(self, member.get_name())
            if member.get_data_type() == 'xs:date':
                newvalue = date_calcs.date_from_string(obj1)
                setattr(self, member.get_name(), newvalue)
            elif member.get_container():
                for child in obj1:
                    if type(child) == types.InstanceType:
                        child.walk_and_update()
            else:
                obj1 = getattr(self, member.get_name())
                if type(obj1) == types.InstanceType:
                    obj1.walk_and_update()
        if people.superclass != None:
          people.superclass.walk_and_update(self)
    def walk_and_show(self, depth):
        global counter
        counter += 1
        depth += 1
        print '%d. class: people  depth: %d' % (counter, depth, )
        members = people._member_data_items
        for member in members:
            s1 = member.get_name()
            s2 = member.get_data_type()
            s3 = '%d' % member.get_container()
            obj1 = getattr(self, member.get_name())
            if member.get_container():
                s4 = '<container>'
            else:
                if type(obj1) != types.InstanceType:
                    s4 = '%s' % obj1
                else:
                    s4 = '<instance>'
            s5 = '%s%s%s  %s' % (s1.ljust(16), s2.ljust(16), s3.rjust(4), s4, )
            print '   ', s5
        for member in members:
            if member.get_container():
                for child in getattr(self, member.get_name()):
                    if type(child) == types.InstanceType:
                        child.walk_and_show(depth)
            else:
                obj1 = getattr(self, member.get_name())
                if type(obj1) == types.InstanceType:
                    obj1.walk_and_show(depth)
    def set_up(self):
        global types, counter
        import types as types_module
        types = types_module
        counter = 0
# end class people


class person:
    _member_data_items = [
        _MemberSpec('name', 'xs:string', 0),
        _MemberSpec('ratio', 'xs:string', 0),
        _MemberSpec('imagesize', 'scale', 0),
        _MemberSpec('interest', 'xs:string', 1),
        _MemberSpec('category', 'xs:integer', 0),
        _MemberSpec('hot_agent', 'hot.agent', 0),
        _MemberSpec('promoter', 'booster', 1),
        _MemberSpec('hot', 'BasicEmptyType', 0),
        ]
    subclass = None
    superclass = None
    def __init__(self, id=-1, value='', ratio_attr='', name='', ratio='', imagesize=None, interest=None, category=-1, hot_agent=None, promoter=None, hot=None):
        self.id = id
        self.value = value
        self.ratio_attr = ratio_attr
        self.name = name
        self.ratio = ratio
        self.imagesize = imagesize
        if interest is None:
            self.interest = []
        else:
            self.interest = interest
        self.category = category
        self.hot_agent = hot_agent
        if promoter is None:
            self.promoter = []
        else:
            self.promoter = promoter
        self.hot = hot
        self.anyAttributes_ = {}
    def factory(*args_, **kwargs_):
        if person.subclass:
            return person.subclass(*args_, **kwargs_)
        else:
            return person(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_name(self): return self.name
    def set_name(self, name): self.name = name
    def get_ratio(self): return self.ratio
    def set_ratio(self, ratio): self.ratio = ratio
    def validate_ratio(self, value):
        # validate type ratio
        pass
    def get_imagesize(self): return self.imagesize
    def set_imagesize(self, imagesize): self.imagesize = imagesize
    def validate_scale(self, value):
        # validate type scale
        pass
    def get_interest(self): return self.interest
    def set_interest(self, interest): self.interest = interest
    def add_interest(self, value): self.interest.append(value)
    def insert_interest(self, index, value): self.interest[index] = value
    def get_category(self): return self.category
    def set_category(self, category): self.category = category
    def get_hot_agent(self): return self.hot_agent
    def set_hot_agent(self, hot_agent): self.hot_agent = hot_agent
    def get_promoter(self): return self.promoter
    def set_promoter(self, promoter): self.promoter = promoter
    def add_promoter(self, value): self.promoter.append(value)
    def insert_promoter(self, index, value): self.promoter[index] = value
    def get_hot(self): return self.hot
    def set_hot(self, hot): self.hot = hot
    def get_id(self): return self.id
    def set_id(self, id): self.id = id
    def get_value(self): return self.value
    def set_value(self, value): self.value = value
    def get_ratio_attr(self): return self.ratio_attr
    def set_ratio_attr(self, ratio_attr): self.ratio_attr = ratio_attr
    def getAnyAttributes_(self): return self.anyAttributes_
    def setAnyAttributes_(self, anyAttributes_): self.anyAttributes_ = anyAttributes_
    def export(self, outfile, level, name_='person', namespace_=''):
        showIndent(outfile, level)
        outfile.write('<%s%s' % (namespace_, name_))
        self.exportAttributes(outfile, level, name_='person', namespace_='')
        outfile.write('>\n')
        self.exportChildren(outfile, level + 1, name_, namespace_)
        showIndent(outfile, level)
        outfile.write('</%s%s>\n' % (namespace_, name_))
    def exportAttributes(self, outfile, level, name_='person', namespace_=''):
        if self.get_id() is not None:
            outfile.write(' id="%s"' % (quote_attrib(self.get_id()), ))
        if self.get_value() is not None:
            outfile.write(' value="%s"' % (quote_attrib(self.get_value()), ))
        if self.get_ratio_attr() is not None:
            outfile.write(' ratio_attr="%s"' % (quote_attrib(self.get_ratio_attr()), ))
        for name, value in self.anyAttributes_.items():
            outfile.write(' %s="%s"' % (name, quote_attrib(value), ))
    def exportChildren(self, outfile, level, name_='person', namespace_=''):
        if self.get_name() != None :
            if self.get_name() != "" :
                showIndent(outfile, level)
                outfile.write('<name>%s</name>\n' % quote_xml(self.get_name()))
        showIndent(outfile, level)
        outfile.write('<ratio>%s</ratio>\n' % quote_xml(self.get_ratio()))
        if self.imagesize:
            self.imagesize.export(outfile, level, name_='imagesize', namespace_='')
        for interest_ in self.get_interest():
            showIndent(outfile, level)
            outfile.write('<interest>%s</interest>\n' % quote_xml(interest_))
        showIndent(outfile, level)
        outfile.write('<category>%d</category>\n' % self.get_category())
        if self.hot_agent:
            self.hot_agent.export(outfile, level)
        for promoter_ in self.get_promoter():
            promoter_.export(outfile, level, name_='promoter', namespace_='')
        if self.hot:
            self.hot.export(outfile, level, name_='hot', namespace_='')
    def exportLiteral(self, outfile, level, name_='person'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('id = "%s",\n' % (self.get_id(),))
        showIndent(outfile, level)
        outfile.write('value = "%s",\n' % (self.get_value(),))
        showIndent(outfile, level)
        outfile.write('ratio_attr = "%s",\n' % (self.get_ratio_attr(),))
        for name, value in self.anyAttributes_.items():
            showIndent(outfile, level)
            outfile.write('%s = "%s",\n' % (name, value,))
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('name=%s,\n' % quote_python(self.get_name()))
        showIndent(outfile, level)
        outfile.write('ratio=%s,\n' % quote_python(self.get_ratio()))
        if self.imagesize:
            showIndent(outfile, level)
            outfile.write('imagesize=scale(\n')
            self.imagesize.exportLiteral(outfile, level, name_='imagesize')
            showIndent(outfile, level)
            outfile.write('),\n')
        showIndent(outfile, level)
        outfile.write('interest=[\n')
        level += 1
        for interest in self.interest:
            showIndent(outfile, level)
            outfile.write('%s,\n' % quote_python(interest))
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        showIndent(outfile, level)
        outfile.write('category=%d,\n' % self.get_category())
        if self.hot_agent:
            showIndent(outfile, level)
            outfile.write('hot_agent=hot_agent(\n')
            self.hot_agent.exportLiteral(outfile, level, name_='hot_agent')
            showIndent(outfile, level)
            outfile.write('),\n')
        showIndent(outfile, level)
        outfile.write('promoter=[\n')
        level += 1
        for promoter in self.promoter:
            showIndent(outfile, level)
            outfile.write('booster(\n')
            promoter.exportLiteral(outfile, level, name_='promoter')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        if self.hot:
            showIndent(outfile, level)
            outfile.write('hot=BasicEmptyType(\n')
            self.hot.exportLiteral(outfile, level, name_='hot')
            showIndent(outfile, level)
            outfile.write('),\n')
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        if attrs.get('id'):
            try:
                self.id = int(attrs.get('id').value)
            except ValueError:
                raise ValueError('Bad integer attribute (id)')
        if attrs.get('value'):
            self.value = attrs.get('value').value
        if attrs.get('ratio_attr'):
            self.ratio_attr = attrs.get('ratio_attr').value
        self.anyAttributes_ = {}
        for name, value in attrs.items():
            if name != "id" and name != "value" and name != "ratio_attr":
                self.anyAttributes_[name] = value
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'name':
            name_ = ''
            for text__content_ in child_.childNodes:
                name_ += text__content_.nodeValue
            self.name = name_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'ratio':
            ratio_ = ''
            for text__content_ in child_.childNodes:
                ratio_ += text__content_.nodeValue
            self.ratio = ratio_
            self.validate_ratio(self.ratio)    # validate type ratio
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'imagesize':
            obj_ = scale.factory()
            obj_.build(child_)
            self.set_imagesize(obj_)
            self.validate_scale(self.imagesize)    # validate type scale
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'interest':
            interest_ = ''
            for text__content_ in child_.childNodes:
                interest_ += text__content_.nodeValue
            self.interest.append(interest_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'category':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    ival_ = int(sval_)
                except ValueError:
                    raise ValueError('requires integer -- %s' % child_.toxml())
                self.category = ival_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'hot.agent':
            obj_ = hot_agent.factory()
            obj_.build(child_)
            self.set_hot_agent(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'promoter':
            obj_ = booster.factory()
            obj_.build(child_)
            self.promoter.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'hot':
            obj_ = BasicEmptyType.factory()
            obj_.build(child_)
            self.set_hot(obj_)
    def walk_and_update(self):
        members = person._member_data_items
        for member in members:
            obj1 = getattr(self, member.get_name())
            if member.get_data_type() == 'xs:date':
                newvalue = date_calcs.date_from_string(obj1)
                setattr(self, member.get_name(), newvalue)
            elif member.get_container():
                for child in obj1:
                    if type(child) == types.InstanceType:
                        child.walk_and_update()
            else:
                obj1 = getattr(self, member.get_name())
                if type(obj1) == types.InstanceType:
                    obj1.walk_and_update()
        if person.superclass != None:
          person.superclass.walk_and_update(self)
    def walk_and_show(self, depth):
        global counter
        counter += 1
        depth += 1
        print '%d. class: person  depth: %d' % (counter, depth, )
        members = person._member_data_items
        for member in members:
            s1 = member.get_name()
            s2 = member.get_data_type()
            s3 = '%d' % member.get_container()
            obj1 = getattr(self, member.get_name())
            if member.get_container():
                s4 = '<container>'
            else:
                if type(obj1) != types.InstanceType:
                    s4 = '%s' % obj1
                else:
                    s4 = '<instance>'
            s5 = '%s%s%s  %s' % (s1.ljust(16), s2.ljust(16), s3.rjust(4), s4, )
            print '   ', s5
        for member in members:
            if member.get_container():
                for child in getattr(self, member.get_name()):
                    if type(child) == types.InstanceType:
                        child.walk_and_show(depth)
            else:
                obj1 = getattr(self, member.get_name())
                if type(obj1) == types.InstanceType:
                    obj1.walk_and_show(depth)
# end class person


class scale:
    _member_data_items = [
        ]
    subclass = None
    superclass = None
    def __init__(self, valueOf_=''):
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if scale.subclass:
            return scale.subclass(*args_, **kwargs_)
        else:
            return scale(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getValueOf_(self): return self.valueOf_
    def setValueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def export(self, outfile, level, name_='scale', namespace_=''):
        showIndent(outfile, level)
        outfile.write('<%s%s>' % (namespace_, name_))
        self.exportChildren(outfile, level + 1, name_, namespace_)
        outfile.write('</%s%s>\n' % (namespace_, name_))
    def exportAttributes(self, outfile, level, name_='scale', namespace_=''):
        pass
    def exportChildren(self, outfile, level, name_='scale', namespace_=''):
        outfile.write(quote_xml(self.valueOf_))
    def exportLiteral(self, outfile, level, name_='scale'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('valueOf_ = "%s",\n' % (self.valueOf_,))
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        self.valueOf_ = ''
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        pass
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.TEXT_NODE:
            self.valueOf_ += child_.nodeValue
    def walk_and_update(self):
        members = scale._member_data_items
        for member in members:
            obj1 = getattr(self, member.get_name())
            if member.get_data_type() == 'xs:date':
                newvalue = date_calcs.date_from_string(obj1)
                setattr(self, member.get_name(), newvalue)
            elif member.get_container():
                for child in obj1:
                    if type(child) == types.InstanceType:
                        child.walk_and_update()
            else:
                obj1 = getattr(self, member.get_name())
                if type(obj1) == types.InstanceType:
                    obj1.walk_and_update()
        if scale.superclass != None:
          scale.superclass.walk_and_update(self)
    def walk_and_show(self, depth):
        global counter
        counter += 1
        depth += 1
        print '%d. class: scale  depth: %d' % (counter, depth, )
        members = scale._member_data_items
        for member in members:
            s1 = member.get_name()
            s2 = member.get_data_type()
            s3 = '%d' % member.get_container()
            obj1 = getattr(self, member.get_name())
            if member.get_container():
                s4 = '<container>'
            else:
                if type(obj1) != types.InstanceType:
                    s4 = '%s' % obj1
                else:
                    s4 = '<instance>'
            s5 = '%s%s%s  %s' % (s1.ljust(16), s2.ljust(16), s3.rjust(4), s4, )
            print '   ', s5
        for member in members:
            if member.get_container():
                for child in getattr(self, member.get_name()):
                    if type(child) == types.InstanceType:
                        child.walk_and_show(depth)
            else:
                obj1 = getattr(self, member.get_name())
                if type(obj1) == types.InstanceType:
                    obj1.walk_and_show(depth)
# end class scale


class BasicEmptyType:
    _member_data_items = [
        ]
    subclass = None
    superclass = None
    def __init__(self, valueOf_=''):
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if BasicEmptyType.subclass:
            return BasicEmptyType.subclass(*args_, **kwargs_)
        else:
            return BasicEmptyType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getValueOf_(self): return self.valueOf_
    def setValueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def export(self, outfile, level, name_='BasicEmptyType', namespace_=''):
        showIndent(outfile, level)
        outfile.write('<%s%s>' % (namespace_, name_))
        self.exportChildren(outfile, level + 1, name_, namespace_)
        outfile.write('</%s%s>\n' % (namespace_, name_))
    def exportAttributes(self, outfile, level, name_='BasicEmptyType', namespace_=''):
        pass
    def exportChildren(self, outfile, level, name_='BasicEmptyType', namespace_=''):
        outfile.write(quote_xml(self.valueOf_))
    def exportLiteral(self, outfile, level, name_='BasicEmptyType'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('valueOf_ = "%s",\n' % (self.valueOf_,))
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        self.valueOf_ = ''
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        pass
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.TEXT_NODE:
            self.valueOf_ += child_.nodeValue
    def walk_and_update(self):
        members = BasicEmptyType._member_data_items
        for member in members:
            obj1 = getattr(self, member.get_name())
            if member.get_data_type() == 'xs:date':
                newvalue = date_calcs.date_from_string(obj1)
                setattr(self, member.get_name(), newvalue)
            elif member.get_container():
                for child in obj1:
                    if type(child) == types.InstanceType:
                        child.walk_and_update()
            else:
                obj1 = getattr(self, member.get_name())
                if type(obj1) == types.InstanceType:
                    obj1.walk_and_update()
        if BasicEmptyType.superclass != None:
          BasicEmptyType.superclass.walk_and_update(self)
    def walk_and_show(self, depth):
        global counter
        counter += 1
        depth += 1
        print '%d. class: BasicEmptyType  depth: %d' % (counter, depth, )
        members = BasicEmptyType._member_data_items
        for member in members:
            s1 = member.get_name()
            s2 = member.get_data_type()
            s3 = '%d' % member.get_container()
            obj1 = getattr(self, member.get_name())
            if member.get_container():
                s4 = '<container>'
            else:
                if type(obj1) != types.InstanceType:
                    s4 = '%s' % obj1
                else:
                    s4 = '<instance>'
            s5 = '%s%s%s  %s' % (s1.ljust(16), s2.ljust(16), s3.rjust(4), s4, )
            print '   ', s5
        for member in members:
            if member.get_container():
                for child in getattr(self, member.get_name()):
                    if type(child) == types.InstanceType:
                        child.walk_and_show(depth)
            else:
                obj1 = getattr(self, member.get_name())
                if type(obj1) == types.InstanceType:
                    obj1.walk_and_show(depth)
# end class BasicEmptyType


class hot_agent:
    _member_data_items = [
        _MemberSpec('firstname', 'xs:string', 0),
        _MemberSpec('lastname', 'xs:string', 0),
        _MemberSpec('priority', 'xs:float', 0),
        ]
    subclass = None
    superclass = None
    def __init__(self, firstname='', lastname='', priority=0.0):
        self.firstname = firstname
        self.lastname = lastname
        self.priority = priority
        self.anyAttributes_ = {}
    def factory(*args_, **kwargs_):
        if hot_agent.subclass:
            return hot_agent.subclass(*args_, **kwargs_)
        else:
            return hot_agent(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_firstname(self): return self.firstname
    def set_firstname(self, firstname): self.firstname = firstname
    def get_lastname(self): return self.lastname
    def set_lastname(self, lastname): self.lastname = lastname
    def get_priority(self): return self.priority
    def set_priority(self, priority): self.priority = priority
    def getAnyAttributes_(self): return self.anyAttributes_
    def setAnyAttributes_(self, anyAttributes_): self.anyAttributes_ = anyAttributes_
    def export(self, outfile, level, name_='hot.agent', namespace_=''):
        showIndent(outfile, level)
        outfile.write('<%s%s' % (namespace_, name_))
        self.exportAttributes(outfile, level, name_='hot.agent', namespace_='')
        outfile.write('>\n')
        self.exportChildren(outfile, level + 1, name_, namespace_)
        showIndent(outfile, level)
        outfile.write('</%s%s>\n' % (namespace_, name_))
    def exportAttributes(self, outfile, level, name_='hot.agent', namespace_=''):
        for name, value in self.anyAttributes_.items():
            outfile.write(' %s="%s"' % (name, quote_attrib(value), ))
        pass
    def exportChildren(self, outfile, level, name_='hot.agent', namespace_=''):
        showIndent(outfile, level)
        outfile.write('<firstname>%s</firstname>\n' % quote_xml(self.get_firstname()))
        showIndent(outfile, level)
        outfile.write('<lastname>%s</lastname>\n' % quote_xml(self.get_lastname()))
        showIndent(outfile, level)
        outfile.write('<priority>%f</priority>\n' % self.get_priority())
    def exportLiteral(self, outfile, level, name_='hot.agent'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        for name, value in self.anyAttributes_.items():
            showIndent(outfile, level)
            outfile.write('%s = "%s",\n' % (name, value,))
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('firstname=%s,\n' % quote_python(self.get_firstname()))
        showIndent(outfile, level)
        outfile.write('lastname=%s,\n' % quote_python(self.get_lastname()))
        showIndent(outfile, level)
        outfile.write('priority=%f,\n' % self.get_priority())
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        self.anyAttributes_ = {}
        for name, value in attrs.items():
            self.anyAttributes_[name] = value
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'firstname':
            firstname_ = ''
            for text__content_ in child_.childNodes:
                firstname_ += text__content_.nodeValue
            self.firstname = firstname_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'lastname':
            lastname_ = ''
            for text__content_ in child_.childNodes:
                lastname_ += text__content_.nodeValue
            self.lastname = lastname_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'priority':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self.priority = fval_
    def walk_and_update(self):
        members = hot_agent._member_data_items
        for member in members:
            obj1 = getattr(self, member.get_name())
            if member.get_data_type() == 'xs:date':
                newvalue = date_calcs.date_from_string(obj1)
                setattr(self, member.get_name(), newvalue)
            elif member.get_container():
                for child in obj1:
                    if type(child) == types.InstanceType:
                        child.walk_and_update()
            else:
                obj1 = getattr(self, member.get_name())
                if type(obj1) == types.InstanceType:
                    obj1.walk_and_update()
        if hot_agent.superclass != None:
          hot_agent.superclass.walk_and_update(self)
    def walk_and_show(self, depth):
        global counter
        counter += 1
        depth += 1
        print '%d. class: hot_agent  depth: %d' % (counter, depth, )
        members = hot_agent._member_data_items
        for member in members:
            s1 = member.get_name()
            s2 = member.get_data_type()
            s3 = '%d' % member.get_container()
            obj1 = getattr(self, member.get_name())
            if member.get_container():
                s4 = '<container>'
            else:
                if type(obj1) != types.InstanceType:
                    s4 = '%s' % obj1
                else:
                    s4 = '<instance>'
            s5 = '%s%s%s  %s' % (s1.ljust(16), s2.ljust(16), s3.rjust(4), s4, )
            print '   ', s5
        for member in members:
            if member.get_container():
                for child in getattr(self, member.get_name()):
                    if type(child) == types.InstanceType:
                        child.walk_and_show(depth)
            else:
                obj1 = getattr(self, member.get_name())
                if type(obj1) == types.InstanceType:
                    obj1.walk_and_show(depth)
# end class hot_agent


class booster:
    _member_data_items = [
        _MemberSpec('firstname', 'xs:string', 0),
        _MemberSpec('lastname', 'xs:string', 0),
        _MemberSpec('client', 'client', 1),
        ]
    subclass = None
    superclass = None
    def __init__(self, firstname='', lastname='', client=None):
        self.firstname = firstname
        self.lastname = lastname
        if client is None:
            self.client = []
        else:
            self.client = client
    def factory(*args_, **kwargs_):
        if booster.subclass:
            return booster.subclass(*args_, **kwargs_)
        else:
            return booster(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_firstname(self): return self.firstname
    def set_firstname(self, firstname): self.firstname = firstname
    def get_lastname(self): return self.lastname
    def set_lastname(self, lastname): self.lastname = lastname
    def get_client(self): return self.client
    def set_client(self, client): self.client = client
    def add_client(self, value): self.client.append(value)
    def insert_client(self, index, value): self.client[index] = value
    def export(self, outfile, level, name_='booster', namespace_=''):
        showIndent(outfile, level)
        outfile.write('<%s%s>\n' % (namespace_, name_))
        self.exportChildren(outfile, level + 1, name_, namespace_)
        showIndent(outfile, level)
        outfile.write('</%s%s>\n' % (namespace_, name_))
    def exportAttributes(self, outfile, level, name_='booster', namespace_=''):
        pass
    def exportChildren(self, outfile, level, name_='booster', namespace_=''):
        showIndent(outfile, level)
        outfile.write('<firstname>%s</firstname>\n' % quote_xml(self.get_firstname()))
        showIndent(outfile, level)
        outfile.write('<lastname>%s</lastname>\n' % quote_xml(self.get_lastname()))
        for client_ in self.get_client():
            client_.export(outfile, level)
    def exportLiteral(self, outfile, level, name_='booster'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('firstname=%s,\n' % quote_python(self.get_firstname()))
        showIndent(outfile, level)
        outfile.write('lastname=%s,\n' % quote_python(self.get_lastname()))
        showIndent(outfile, level)
        outfile.write('client=[\n')
        level += 1
        for client in self.client:
            showIndent(outfile, level)
            outfile.write('client(\n')
            client.exportLiteral(outfile, level)
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        pass
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'firstname':
            firstname_ = ''
            for text__content_ in child_.childNodes:
                firstname_ += text__content_.nodeValue
            self.firstname = firstname_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'lastname':
            lastname_ = ''
            for text__content_ in child_.childNodes:
                lastname_ += text__content_.nodeValue
            self.lastname = lastname_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'client':
            obj_ = client.factory()
            obj_.build(child_)
            self.client.append(obj_)
    def walk_and_update(self):
        members = booster._member_data_items
        for member in members:
            obj1 = getattr(self, member.get_name())
            if member.get_data_type() == 'xs:date':
                newvalue = date_calcs.date_from_string(obj1)
                setattr(self, member.get_name(), newvalue)
            elif member.get_container():
                for child in obj1:
                    if type(child) == types.InstanceType:
                        child.walk_and_update()
            else:
                obj1 = getattr(self, member.get_name())
                if type(obj1) == types.InstanceType:
                    obj1.walk_and_update()
        if booster.superclass != None:
          booster.superclass.walk_and_update(self)
    def walk_and_show(self, depth):
        global counter
        counter += 1
        depth += 1
        print '%d. class: booster  depth: %d' % (counter, depth, )
        members = booster._member_data_items
        for member in members:
            s1 = member.get_name()
            s2 = member.get_data_type()
            s3 = '%d' % member.get_container()
            obj1 = getattr(self, member.get_name())
            if member.get_container():
                s4 = '<container>'
            else:
                if type(obj1) != types.InstanceType:
                    s4 = '%s' % obj1
                else:
                    s4 = '<instance>'
            s5 = '%s%s%s  %s' % (s1.ljust(16), s2.ljust(16), s3.rjust(4), s4, )
            print '   ', s5
        for member in members:
            if member.get_container():
                for child in getattr(self, member.get_name()):
                    if type(child) == types.InstanceType:
                        child.walk_and_show(depth)
            else:
                obj1 = getattr(self, member.get_name())
                if type(obj1) == types.InstanceType:
                    obj1.walk_and_show(depth)
# end class booster


class client:
    _member_data_items = [
        _MemberSpec('fullname', 'xs:string', 0),
        _MemberSpec('refid', 'xs:integer', 0),
        ]
    subclass = None
    superclass = None
    def __init__(self, fullname='', refid=-1):
        self.fullname = fullname
        self.refid = refid
    def factory(*args_, **kwargs_):
        if client.subclass:
            return client.subclass(*args_, **kwargs_)
        else:
            return client(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_fullname(self): return self.fullname
    def set_fullname(self, fullname): self.fullname = fullname
    def get_refid(self): return self.refid
    def set_refid(self, refid): self.refid = refid
    def export(self, outfile, level, name_='client', namespace_=''):
        showIndent(outfile, level)
        outfile.write('<%s%s>\n' % (namespace_, name_))
        self.exportChildren(outfile, level + 1, name_, namespace_)
        showIndent(outfile, level)
        outfile.write('</%s%s>\n' % (namespace_, name_))
    def exportAttributes(self, outfile, level, name_='client', namespace_=''):
        pass
    def exportChildren(self, outfile, level, name_='client', namespace_=''):
        showIndent(outfile, level)
        outfile.write('<fullname>%s</fullname>\n' % quote_xml(self.get_fullname()))
        showIndent(outfile, level)
        outfile.write('<refid>%d</refid>\n' % self.get_refid())
    def exportLiteral(self, outfile, level, name_='client'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('fullname=%s,\n' % quote_python(self.get_fullname()))
        showIndent(outfile, level)
        outfile.write('refid=%d,\n' % self.get_refid())
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        pass
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'fullname':
            fullname_ = ''
            for text__content_ in child_.childNodes:
                fullname_ += text__content_.nodeValue
            self.fullname = fullname_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'refid':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    ival_ = int(sval_)
                except ValueError:
                    raise ValueError('requires integer -- %s' % child_.toxml())
                self.refid = ival_
    def walk_and_update(self):
        members = client._member_data_items
        for member in members:
            obj1 = getattr(self, member.get_name())
            if member.get_data_type() == 'xs:date':
                newvalue = date_calcs.date_from_string(obj1)
                setattr(self, member.get_name(), newvalue)
            elif member.get_container():
                for child in obj1:
                    if type(child) == types.InstanceType:
                        child.walk_and_update()
            else:
                obj1 = getattr(self, member.get_name())
                if type(obj1) == types.InstanceType:
                    obj1.walk_and_update()
        if client.superclass != None:
          client.superclass.walk_and_update(self)
    def walk_and_show(self, depth):
        global counter
        counter += 1
        depth += 1
        print '%d. class: client  depth: %d' % (counter, depth, )
        members = client._member_data_items
        for member in members:
            s1 = member.get_name()
            s2 = member.get_data_type()
            s3 = '%d' % member.get_container()
            obj1 = getattr(self, member.get_name())
            if member.get_container():
                s4 = '<container>'
            else:
                if type(obj1) != types.InstanceType:
                    s4 = '%s' % obj1
                else:
                    s4 = '<instance>'
            s5 = '%s%s%s  %s' % (s1.ljust(16), s2.ljust(16), s3.rjust(4), s4, )
            print '   ', s5
        for member in members:
            if member.get_container():
                for child in getattr(self, member.get_name()):
                    if type(child) == types.InstanceType:
                        child.walk_and_show(depth)
            else:
                obj1 = getattr(self, member.get_name())
                if type(obj1) == types.InstanceType:
                    obj1.walk_and_show(depth)
# end class client


class Richtlinie:
    _member_data_items = [
        ]
    subclass = None
    superclass = None
    def __init__(self, valueOf_=''):
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if Richtlinie.subclass:
            return Richtlinie.subclass(*args_, **kwargs_)
        else:
            return Richtlinie(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getValueOf_(self): return self.valueOf_
    def setValueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def export(self, outfile, level, name_='Richtlinie', namespace_=''):
        showIndent(outfile, level)
        outfile.write('<%s%s>' % (namespace_, name_))
        self.exportChildren(outfile, level + 1, name_, namespace_)
        outfile.write('</%s%s>\n' % (namespace_, name_))
    def exportAttributes(self, outfile, level, name_='Richtlinie', namespace_=''):
        pass
    def exportChildren(self, outfile, level, name_='Richtlinie', namespace_=''):
        outfile.write(quote_xml(self.valueOf_))
    def exportLiteral(self, outfile, level, name_='Richtlinie'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('valueOf_ = "%s",\n' % (self.valueOf_,))
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        self.valueOf_ = ''
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        pass
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.TEXT_NODE:
            self.valueOf_ += child_.nodeValue
    def walk_and_update(self):
        members = Richtlinie._member_data_items
        for member in members:
            obj1 = getattr(self, member.get_name())
            if member.get_data_type() == 'xs:date':
                newvalue = date_calcs.date_from_string(obj1)
                setattr(self, member.get_name(), newvalue)
            elif member.get_container():
                for child in obj1:
                    if type(child) == types.InstanceType:
                        child.walk_and_update()
            else:
                obj1 = getattr(self, member.get_name())
                if type(obj1) == types.InstanceType:
                    obj1.walk_and_update()
        if Richtlinie.superclass != None:
          Richtlinie.superclass.walk_and_update(self)
    def walk_and_show(self, depth):
        global counter
        counter += 1
        depth += 1
        print '%d. class: Richtlinie  depth: %d' % (counter, depth, )
        members = Richtlinie._member_data_items
        for member in members:
            s1 = member.get_name()
            s2 = member.get_data_type()
            s3 = '%d' % member.get_container()
            obj1 = getattr(self, member.get_name())
            if member.get_container():
                s4 = '<container>'
            else:
                if type(obj1) != types.InstanceType:
                    s4 = '%s' % obj1
                else:
                    s4 = '<instance>'
            s5 = '%s%s%s  %s' % (s1.ljust(16), s2.ljust(16), s3.rjust(4), s4, )
            print '   ', s5
        for member in members:
            if member.get_container():
                for child in getattr(self, member.get_name()):
                    if type(child) == types.InstanceType:
                        child.walk_and_show(depth)
            else:
                obj1 = getattr(self, member.get_name())
                if type(obj1) == types.InstanceType:
                    obj1.walk_and_show(depth)
# end class Richtlinie


from xml.sax import handler, make_parser

class SaxStackElement:
    def __init__(self, name='', obj=None):
        self.name = name
        self.obj = obj
        self.content = ''

#
# SAX handler
#
class Sax_peopleHandler(handler.ContentHandler):
    def __init__(self):
        self.stack = []
        self.root = None

    def getRoot(self):
        return self.root

    def setDocumentLocator(self, locator):
        self.locator = locator
    
    def showError(self, msg):
        print '*** (showError):', msg
        sys.exit(-1)

    def startElement(self, name, attrs):
        done = 0
        if name == 'people':
            obj = people.factory()
            stackObj = SaxStackElement('people', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'person':
            obj = person.factory()
            val = attrs.get('id', None)
            if val is not None:
                try:
                    obj.set_id(int(val))
                except:
                    self.reportError('"id" attribute must be integer')
            val = attrs.get('value', None)
            if val is not None:
                obj.set_value(val)
            val = attrs.get('ratio_attr', None)
            if val is not None:
                obj.set_ratio_attr(val)
            stackObj = SaxStackElement('person', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'name':
            stackObj = SaxStackElement('name', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'ratio':
            stackObj = SaxStackElement('ratio', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'imagesize':
            obj = scale.factory()
            stackObj = SaxStackElement('imagesize', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'interest':
            stackObj = SaxStackElement('interest', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'category':
            stackObj = SaxStackElement('category', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'hot.agent':
            obj = hot_agent.factory()
            stackObj = SaxStackElement('hot_agent', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'promoter':
            obj = booster.factory()
            stackObj = SaxStackElement('promoter', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'hot':
            obj = BasicEmptyType.factory()
            stackObj = SaxStackElement('hot', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'firstname':
            stackObj = SaxStackElement('firstname', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'lastname':
            stackObj = SaxStackElement('lastname', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'priority':
            stackObj = SaxStackElement('priority', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'client':
            obj = client.factory()
            stackObj = SaxStackElement('client', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'fullname':
            stackObj = SaxStackElement('fullname', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'refid':
            stackObj = SaxStackElement('refid', None)
            self.stack.append(stackObj)
            done = 1
        if not done:
            self.reportError('"%s" element not allowed here.' % name)

    def endElement(self, name):
        done = 0
        if name == 'people':
            if len(self.stack) == 1:
                self.root = self.stack[-1].obj
                self.stack.pop()
                done = 1
        elif name == 'person':
            if len(self.stack) >= 2:
                self.stack[-2].obj.add_person(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'name':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.set_name(content)
                self.stack.pop()
                done = 1
        elif name == 'ratio':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.set_ratio(content)
                self.stack.pop()
                done = 1
        elif name == 'imagesize':
            if len(self.stack) >= 2:
                self.stack[-2].obj.set_imagesize(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'interest':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.add_interest(content)
                self.stack.pop()
                done = 1
        elif name == 'category':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                if content:
                    try:
                        content = int(content)
                    except:
                        self.reportError('"category" must be integer -- content: %s' % content)
                else:
                    content = -1
                self.stack[-2].obj.set_category(content)
                self.stack.pop()
                done = 1
        elif name == 'hot.agent':
            if len(self.stack) >= 2:
                self.stack[-2].obj.set_hot_agent(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'promoter':
            if len(self.stack) >= 2:
                self.stack[-2].obj.add_promoter(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'hot':
            if len(self.stack) >= 2:
                self.stack[-2].obj.set_hot(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'firstname':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.set_firstname(content)
                self.stack.pop()
                done = 1
        elif name == 'lastname':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.set_lastname(content)
                self.stack.pop()
                done = 1
        elif name == 'priority':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                if content:
                    try:
                        content = float(content)
                    except:
                        self.reportError('"priority" must be float -- content: %s' % content)
                else:
                    content = -1
                self.stack[-2].obj.set_priority(content)
                self.stack.pop()
                done = 1
        elif name == 'client':
            if len(self.stack) >= 2:
                self.stack[-2].obj.add_client(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'fullname':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.set_fullname(content)
                self.stack.pop()
                done = 1
        elif name == 'refid':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                if content:
                    try:
                        content = int(content)
                    except:
                        self.reportError('"refid" must be integer -- content: %s' % content)
                else:
                    content = -1
                self.stack[-2].obj.set_refid(content)
                self.stack.pop()
                done = 1
        if not done:
            self.reportError('"%s" element not allowed here.' % name)

    def characters(self, chrs, start, end):
        if len(self.stack) > 0:
            self.stack[-1].content += chrs[start:end]

    def reportError(self, mesg):
        locator = self.locator
        sys.stderr.write('Doc: %s  Line: %d  Column: %d\n' % \
            (locator.getSystemId(), locator.getLineNumber(), 
            locator.getColumnNumber() + 1))
        sys.stderr.write(mesg)
        sys.stderr.write('\n')
        sys.exit(-1)
        #raise RuntimeError

USAGE_TEXT = """
Usage: python <Parser>.py [ -s ] <in_xml_file>
Options:
    -s        Use the SAX parser, not the minidom parser.
"""

def usage():
    print USAGE_TEXT
    sys.exit(-1)


#
# SAX handler used to determine the top level element.
#
class SaxSelectorHandler(handler.ContentHandler):
    def __init__(self):
        self.topElementName = None
    def getTopElementName(self):
        return self.topElementName
    def startElement(self, name, attrs):
        self.topElementName = name
        raise StopIteration


def parseSelect(inFileName):
    infile = file(inFileName, 'r')
    topElementName = None
    parser = make_parser()
    documentHandler = SaxSelectorHandler()
    parser.setContentHandler(documentHandler)
    try:
        try:
            parser.parse(infile)
        except StopIteration:
            topElementName = documentHandler.getTopElementName()
        if topElementName is None:
            raise RuntimeError, 'no top level element'
        topElementName = topElementName.replace('-', '_').replace(':', '_')
        if topElementName not in globals():
            raise RuntimeError, 'no class for top element: %s' % topElementName
        topElement = globals()[topElementName]
        infile.seek(0)
        doc = minidom.parse(infile)
    finally:
        infile.close()
    rootNode = doc.childNodes[0]
    rootObj = topElement.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    sys.stdout.write('<?xml version="1.0" ?>\n')
    rootObj.export(sys.stdout, 0)
    return rootObj


def saxParse(inFileName):
    parser = make_parser()
    documentHandler = Sax_peopleHandler()
    parser.setDocumentHandler(documentHandler)
    parser.parse('file:%s' % inFileName)
    root = documentHandler.getRoot()
    sys.stdout.write('<?xml version="1.0" ?>\n')
    root.export(sys.stdout, 0)
    return root


def saxParseString(inString):
    parser = make_parser()
    documentHandler = Sax_peopleHandler()
    parser.setDocumentHandler(documentHandler)
    parser.feed(inString)
    parser.close()
    rootObj = documentHandler.getRoot()
    #sys.stdout.write('<?xml version="1.0" ?>\n')
    #rootObj.export(sys.stdout, 0)
    return rootObj


def parse(inFileName):
    doc = minidom.parse(inFileName)
    rootNode = doc.documentElement
    rootObj = people.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    sys.stdout.write('<?xml version="1.0" ?>\n')
    rootObj.export(sys.stdout, 0, name_="people")
    return rootObj


def parseString(inString):
    doc = minidom.parseString(inString)
    rootNode = doc.documentElement
    rootObj = people.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    sys.stdout.write('<?xml version="1.0" ?>\n')
    rootObj.export(sys.stdout, 0, name_="people")
    return rootObj


def parseLiteral(inFileName):
    doc = minidom.parse(inFileName)
    rootNode = doc.documentElement
    rootObj = people.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    sys.stdout.write('from out2sup import *\n\n')
    sys.stdout.write('rootObj = people(\n')
    rootObj.exportLiteral(sys.stdout, 0, name_="people")
    sys.stdout.write(')\n')
    return rootObj


def main():
    args = sys.argv[1:]
    if len(args) == 2 and args[0] == '-s':
        saxParse(args[1])
    elif len(args) == 1:
        parse(args[0])
    else:
        usage()


if __name__ == '__main__':
    main()
    #import pdb
    #pdb.run('main()')

