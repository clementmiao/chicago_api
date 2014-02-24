from django import template

register = template.Library()

@register.inclusion_tag('gmap/map.html')
def gmap(html_id, latitude, longitude, **kwargs):
    """
    {% gmap <html_id> <latitude> <longitude> [zoom=<zoom>] [map_type=<map_type>]
    [data=[<map_data>] %}
    """
    zoom = kwargs.get('zoom', 15)
    map_type = kwargs.get('map_type', 'ROADMAP')
    m_data = kwargs.get('data')
    data = {
        'html_id': html_id,
        'latitude': latitude,
        'longitude': longitude,
        'zoom': zoom,
        'map_type': map_type
    }

    if m_data:
        data['data'] = m_data

    return data