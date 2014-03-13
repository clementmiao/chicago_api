from django import template

register = template.Library()

@register.inclusion_tag('gmap/map_sentiment.html')

def gmap_sentiment(html_id, latitude, longitude, kml, **kwargs):
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
        'map_type': map_type,
        'kml': kml
    }

    if m_data:
        data['data'] = m_data

    return data