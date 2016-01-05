from django import template

register = template.Library()

@register.simple_tag
def table_head_tag(name, title):
    th = '''<th><a href="" ng-click = "sort('%s')">
    %s
    <i class = "glyphicon" ng-class="{'glyphicon-chevron-up':isSortUp('%s'), 'glyphicon glyphicon-chevron-down':isSortDown('%s')}"></i></a></th>''' %(name, title, name, name)
    return th
