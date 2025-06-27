# AUTO GENERATED FILE - DO NOT EDIT

import typing  # noqa: F401
from typing_extensions import TypedDict, NotRequired, Literal # noqa: F401
from dash.development.base_component import Component, _explicitize_args

ComponentType = typing.Union[
    str,
    int,
    float,
    Component,
    None,
    typing.Sequence[typing.Union[str, int, float, Component, None]],
]

NumberType = typing.Union[
    typing.SupportsFloat, typing.SupportsInt, typing.SupportsComplex
]


class LineChart(Component):
    """A LineChart component.
Mantine-themed line chart built on top of the Recharts library,

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    Additional components that are rendered inside recharts
    `AreaChart` component.

- id (string; optional):
    Unique ID to identify this component in Dash callbacks.

- activeDotProps (boolean | number | string | dict | list; optional):
    Props passed down to all active dots. Ignored if
    `withDots={False}` is set.

- aria-* (string; optional):
    Wild card aria attributes.

- bd (string | number; optional):
    Border.

- bg (optional):
    Background, theme key: theme.colors.

- bga (optional):
    BackgroundAttachment.

- bgp (string | number; optional):
    BackgroundPosition.

- bgr (optional):
    BackgroundRepeat.

- bgsz (string | number; optional):
    BackgroundSize.

- bottom (string | number; optional)

- c (optional):
    Color.

- className (string; optional):
    Class added to the root element, if applicable.

- classNames (dict; optional):
    Adds class names to Mantine components.

- clickData (dict with strings as keys and values of type boolean | number | string | dict | list; optional):
    Click data.

- clickSeriesName (dict with strings as keys and values of type boolean | number | string | dict | list; optional):
    Name of the series that was clicked.

- connectNulls (boolean; optional):
    Determines whether points with `None` values should be connected,
    `True` by default.

- curveType (a value equal to: 'bump', 'linear', 'natural', 'monotone', 'step', 'stepBefore', 'stepAfter'; optional):
    Type of the curve, `'monotone'` by default.

- darkHidden (boolean; optional):
    Determines whether component should be hidden in dark color scheme
    with `display: none`.

- data (list of dicts with strings as keys and values of type boolean | number | string | dict | list; required):
    Data used to display chart.

- data-* (string; optional):
    Wild card data attributes.

- dataKey (string; required):
    Key of the `data` object for x-axis values.

- display (optional)

- dotProps (boolean | number | string | dict | list; optional):
    Props passed down to all dots. Ignored if `withDots={False}` is
    set.

- ff (optional):
    FontFamily.

- fillOpacity (number; optional):
    Controls fill opacity of all lines, `1` by default.

- flex (string | number; optional)

- fs (optional):
    FontStyle.

- fw (optional):
    FontWeight.

- fz (number; optional):
    FontSize, theme key: theme.fontSizes.

- gradientStops (list of dicts; optional):
    Data used to generate gradient stops, [{ offset: 0, color: 'red'
    }, { offset: 100, color: 'blue' }] by default.

    `gradientStops` is a list of dicts with keys:

    - offset (number; required)

    - color (required)

- gridAxis (a value equal to: 'none', 'x', 'y', 'xy'; optional):
    Specifies which lines should be displayed in the grid, `'x'` by
    default.

- gridColor (optional):
    Color of the grid and cursor lines, by default depends on color
    scheme.

- gridProps (dict; optional):
    Props passed down to the `CartesianGrid` component.

- h (string | number; optional):
    Height, theme key: theme.spacing.

- hiddenFrom (optional):
    Breakpoint above which the component is hidden with `display:
    none`.

- highlightHover (boolean; optional):
    Determines whether a hovered series is highlighted. False by
    default. Mirrors the behaviour when hovering about chart legend
    items.

- hoverData (dict with strings as keys and values of type boolean | number | string | dict | list; optional):
    Hover data.

- hoverSeriesName (dict with strings as keys and values of type boolean | number | string | dict | list; optional):
    Name of the series that is hovered.

- inset (string | number; optional)

- left (string | number; optional)

- legendProps (dict; optional):
    Props passed down to the `Legend` component.

- lh (number; optional):
    LineHeight, theme key: lineHeights.

- lightHidden (boolean; optional):
    Determines whether component should be hidden in light color
    scheme with `display: none`.

- lineChartProps (boolean | number | string | dict | list; optional):
    Props passed down to recharts `LineChart` component.

- lineProps (boolean | number | string | dict | list; optional):
    Props passed down to recharts `Line` component.

- loading_state (dict; optional):
    Object that holds the loading state object coming from
    dash-renderer. For use with dash<3.

    `loading_state` is a dict with keys:

    - is_loading (boolean; required):
        Determines if the component is loading or not.

    - prop_name (string; required):
        Holds which property is loading.

    - component_name (string; required):
        Holds the name of the component that is loading.

- lts (string | number; optional):
    LetterSpacing.

- m (number; optional):
    Margin, theme key: theme.spacing.

- mah (string | number; optional):
    MaxHeight, theme key: theme.spacing.

- maw (string | number; optional):
    MaxWidth, theme key: theme.spacing.

- mb (number; optional):
    MarginBottom, theme key: theme.spacing.

- me (number; optional):
    MarginInlineEnd, theme key: theme.spacing.

- mih (string | number; optional):
    MinHeight, theme key: theme.spacing.

- miw (string | number; optional):
    MinWidth, theme key: theme.spacing.

- ml (number; optional):
    MarginLeft, theme key: theme.spacing.

- mod (string | dict with strings as keys and values of type boolean | number | string | dict | list; optional):
    Element modifiers transformed into `data-` attributes, for
    example, `{ 'data-size': 'xl' }`, falsy values are removed.

- mr (number; optional):
    MarginRight, theme key: theme.spacing.

- ms (number; optional):
    MarginInlineStart, theme key: theme.spacing.

- mt (number; optional):
    MarginTop, theme key: theme.spacing.

- mx (number; optional):
    MarginInline, theme key: theme.spacing.

- my (number; optional):
    MarginBlock, theme key: theme.spacing.

- opacity (optional)

- orientation (a value equal to: 'horizontal', 'vertical'; optional):
    Chart orientation, `'horizontal'` by default.

- p (number; optional):
    Padding, theme key: theme.spacing.

- pb (number; optional):
    PaddingBottom, theme key: theme.spacing.

- pe (number; optional):
    PaddingInlineEnd, theme key: theme.spacing.

- pl (number; optional):
    PaddingLeft, theme key: theme.spacing.

- pos (optional):
    Position.

- pr (number; optional):
    PaddingRight, theme key: theme.spacing.

- ps (number; optional):
    PaddingInlineStart, theme key: theme.spacing.

- pt (number; optional):
    PaddingTop, theme key: theme.spacing.

- px (number; optional):
    PaddingInline, theme key: theme.spacing.

- py (number; optional):
    PaddingBlock, theme key: theme.spacing.

- referenceLines (list of dicts; optional):
    Reference lines that should be displayed on the chart.

- right (string | number; optional)

- rightYAxisLabel (boolean | number | string | dict | list; optional):
    Props passed down to the YAxis recharts component rendered on the
    right side.

- rightYAxisProps (boolean | number | string | dict | list; optional):
    Props passed down to the YAxis recharts component rendered on the
    right side.

- series (list of dicts; required):
    An array of objects with `name` and `color` keys. Determines which
    data should be consumed from the `data` array.

    `series` is a list of dicts with keys:

    - strokeDasharray (string | number; optional)

    - name (string; required)

    - color (optional)

    - label (string; optional)

    - yAxisId (string; optional)

- strokeDasharray (string | number; optional):
    Dash array for the grid lines and cursor, `'5 5'` by default.

- strokeWidth (number; optional):
    Stroke width for the chart lines, `2` by default.

- styles (boolean | number | string | dict | list; optional):
    Mantine styles API.

- ta (optional):
    TextAlign.

- tabIndex (number; optional):
    tab-index.

- td (string | number; optional):
    TextDecoration.

- textColor (optional):
    Color of the text displayed inside the chart, `'dimmed'` by
    default.

- tickLine (a value equal to: 'none', 'x', 'y', 'xy'; optional):
    Specifies which axis should have tick line, `'y'` by default.

- tooltipAnimationDuration (number; optional):
    Tooltip position animation duration in ms, `0` by default.

- tooltipProps (dict; optional):
    Props passed down to the `Tooltip` component.

- top (string | number; optional)

- tt (optional):
    TextTransform.

- type (a value equal to: 'default', 'gradient'; optional):
    Controls styles of the line 'default' | 'gradient'.   'default' by
    default.

- unit (string; optional):
    Unit displayed next to each tick in y-axis.

- unstyled (boolean; optional):
    Remove all Mantine styling from the component.

- valueFormatter (boolean | number | string | dict | list; optional):
    A function to format values on Y axis and inside the tooltip. See
    https://www.dash-mantine-components.com/functions-as-props.

- variant (string; optional):
    variant.

- visibleFrom (optional):
    Breakpoint below which the component is hidden with `display:
    none`.

- w (string | number; optional):
    Width, theme key: theme.spacing.

- withDots (boolean; optional):
    Determines whether dots should be displayed, `True` by default.

- withLegend (boolean; optional):
    Determines whether chart legend should be displayed, `False` by
    default.

- withPointLabels (boolean; optional):
    Determines whether each point should have associated label, False
    by default.

- withRightYAxis (boolean; optional):
    Determines whether additional y-axis should be displayed on the
    right side of the chart, False by default.

- withTooltip (boolean; optional):
    Determines whether chart tooltip should be displayed, `True` by
    default.

- withXAxis (boolean; optional):
    Determines whether x-axis should be hidden, `True` by default.

- withYAxis (boolean; optional):
    Determines whether y-axis should be hidden, `True` by default.

- xAxisLabel (string; optional):
    A label to display below the x-axis.

- xAxisProps (dict; optional):
    Props passed down to the `XAxis` recharts component.

- yAxisLabel (string; optional):
    A label to display next to the y-axis.

- yAxisProps (dict; optional):
    Props passed down to the `YAxis` recharts component."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_mantine_components'
    _type = 'LineChart'
    Series = TypedDict(
        "Series",
            {
            "strokeDasharray": NotRequired[typing.Union[str, NumberType]],
            "name": str,
            "color": NotRequired[typing.Union[Literal["dark"], Literal["gray"], Literal["red"], Literal["pink"], Literal["grape"], Literal["violet"], Literal["indigo"], Literal["blue"], Literal["cyan"], Literal["green"], Literal["lime"], Literal["yellow"], Literal["orange"], Literal["teal"]]],
            "label": NotRequired[str],
            "yAxisId": NotRequired[str]
        }
    )

    GradientStops = TypedDict(
        "GradientStops",
            {
            "offset": NumberType,
            "color": typing.Union[Literal["dark"], Literal["gray"], Literal["red"], Literal["pink"], Literal["grape"], Literal["violet"], Literal["indigo"], Literal["blue"], Literal["cyan"], Literal["green"], Literal["lime"], Literal["yellow"], Literal["orange"], Literal["teal"]]
        }
    )

    LoadingState = TypedDict(
        "LoadingState",
            {
            "is_loading": bool,
            "prop_name": str,
            "component_name": str
        }
    )


    def __init__(
        self,
        children: typing.Optional[ComponentType] = None,
        data: typing.Optional[typing.Sequence[typing.Dict[typing.Union[str, float, int], typing.Any]]] = None,
        series: typing.Optional[typing.Sequence["Series"]] = None,
        curveType: typing.Optional[Literal["bump", "linear", "natural", "monotone", "step", "stepBefore", "stepAfter"]] = None,
        fillOpacity: typing.Optional[NumberType] = None,
        withDots: typing.Optional[bool] = None,
        dotProps: typing.Optional[typing.Any] = None,
        activeDotProps: typing.Optional[typing.Any] = None,
        strokeWidth: typing.Optional[NumberType] = None,
        lineChartProps: typing.Optional[typing.Any] = None,
        lineProps: typing.Optional[typing.Any] = None,
        connectNulls: typing.Optional[bool] = None,
        clickData: typing.Optional[typing.Dict[typing.Union[str, float, int], typing.Any]] = None,
        hoverData: typing.Optional[typing.Dict[typing.Union[str, float, int], typing.Any]] = None,
        clickSeriesName: typing.Optional[typing.Dict[typing.Union[str, float, int], typing.Any]] = None,
        hoverSeriesName: typing.Optional[typing.Dict[typing.Union[str, float, int], typing.Any]] = None,
        highlightHover: typing.Optional[bool] = None,
        withPointLabels: typing.Optional[bool] = None,
        gradientStops: typing.Optional[typing.Sequence["GradientStops"]] = None,
        type: typing.Optional[Literal["default", "gradient"]] = None,
        className: typing.Optional[str] = None,
        style: typing.Optional[typing.Any] = None,
        hiddenFrom: typing.Optional[typing.Union[Literal["xs"], Literal["sm"], Literal["md"], Literal["lg"], Literal["xl"]]] = None,
        visibleFrom: typing.Optional[typing.Union[Literal["xs"], Literal["sm"], Literal["md"], Literal["lg"], Literal["xl"]]] = None,
        lightHidden: typing.Optional[bool] = None,
        darkHidden: typing.Optional[bool] = None,
        mod: typing.Optional[typing.Union[str, typing.Dict[typing.Union[str, float, int], typing.Any]]] = None,
        m: typing.Optional[typing.Union[NumberType, Literal["xs"], Literal["sm"], Literal["md"], Literal["lg"], Literal["xl"]]] = None,
        my: typing.Optional[typing.Union[NumberType, Literal["xs"], Literal["sm"], Literal["md"], Literal["lg"], Literal["xl"]]] = None,
        mx: typing.Optional[typing.Union[NumberType, Literal["xs"], Literal["sm"], Literal["md"], Literal["lg"], Literal["xl"]]] = None,
        mt: typing.Optional[typing.Union[NumberType, Literal["xs"], Literal["sm"], Literal["md"], Literal["lg"], Literal["xl"]]] = None,
        mb: typing.Optional[typing.Union[NumberType, Literal["xs"], Literal["sm"], Literal["md"], Literal["lg"], Literal["xl"]]] = None,
        ms: typing.Optional[typing.Union[NumberType, Literal["xs"], Literal["sm"], Literal["md"], Literal["lg"], Literal["xl"]]] = None,
        me: typing.Optional[typing.Union[NumberType, Literal["xs"], Literal["sm"], Literal["md"], Literal["lg"], Literal["xl"]]] = None,
        ml: typing.Optional[typing.Union[NumberType, Literal["xs"], Literal["sm"], Literal["md"], Literal["lg"], Literal["xl"]]] = None,
        mr: typing.Optional[typing.Union[NumberType, Literal["xs"], Literal["sm"], Literal["md"], Literal["lg"], Literal["xl"]]] = None,
        p: typing.Optional[typing.Union[NumberType, Literal["xs"], Literal["sm"], Literal["md"], Literal["lg"], Literal["xl"]]] = None,
        py: typing.Optional[typing.Union[NumberType, Literal["xs"], Literal["sm"], Literal["md"], Literal["lg"], Literal["xl"]]] = None,
        px: typing.Optional[typing.Union[NumberType, Literal["xs"], Literal["sm"], Literal["md"], Literal["lg"], Literal["xl"]]] = None,
        pt: typing.Optional[typing.Union[NumberType, Literal["xs"], Literal["sm"], Literal["md"], Literal["lg"], Literal["xl"]]] = None,
        pb: typing.Optional[typing.Union[NumberType, Literal["xs"], Literal["sm"], Literal["md"], Literal["lg"], Literal["xl"]]] = None,
        ps: typing.Optional[typing.Union[NumberType, Literal["xs"], Literal["sm"], Literal["md"], Literal["lg"], Literal["xl"]]] = None,
        pe: typing.Optional[typing.Union[NumberType, Literal["xs"], Literal["sm"], Literal["md"], Literal["lg"], Literal["xl"]]] = None,
        pl: typing.Optional[typing.Union[NumberType, Literal["xs"], Literal["sm"], Literal["md"], Literal["lg"], Literal["xl"]]] = None,
        pr: typing.Optional[typing.Union[NumberType, Literal["xs"], Literal["sm"], Literal["md"], Literal["lg"], Literal["xl"]]] = None,
        bd: typing.Optional[typing.Union[str, NumberType]] = None,
        bg: typing.Optional[typing.Union[Literal["dark"], Literal["gray"], Literal["red"], Literal["pink"], Literal["grape"], Literal["violet"], Literal["indigo"], Literal["blue"], Literal["cyan"], Literal["green"], Literal["lime"], Literal["yellow"], Literal["orange"], Literal["teal"]]] = None,
        c: typing.Optional[typing.Union[Literal["dark"], Literal["gray"], Literal["red"], Literal["pink"], Literal["grape"], Literal["violet"], Literal["indigo"], Literal["blue"], Literal["cyan"], Literal["green"], Literal["lime"], Literal["yellow"], Literal["orange"], Literal["teal"]]] = None,
        opacity: typing.Optional[typing.Union[Literal["-moz-initial"], Literal["inherit"], Literal["initial"], Literal["revert"], Literal["revert-layer"], Literal["unset"]]] = None,
        ff: typing.Optional[typing.Union[Literal["monospace"], Literal["text"], Literal["heading"]]] = None,
        fz: typing.Optional[typing.Union[NumberType, Literal["xs"], Literal["sm"], Literal["md"], Literal["lg"], Literal["xl"], Literal["h2"], Literal["h1"], Literal["h3"], Literal["h4"], Literal["h5"], Literal["h6"]]] = None,
        fw: typing.Optional[typing.Union[Literal["-moz-initial"], Literal["inherit"], Literal["initial"], Literal["revert"], Literal["revert-layer"], Literal["unset"], Literal["bold"], Literal["normal"], Literal["bolder"], Literal["lighter"]]] = None,
        lts: typing.Optional[typing.Union[str, NumberType]] = None,
        ta: typing.Optional[typing.Union[Literal["left"], Literal["right"], Literal["-moz-initial"], Literal["inherit"], Literal["initial"], Literal["revert"], Literal["revert-layer"], Literal["unset"], Literal["-webkit-match-parent"], Literal["center"], Literal["end"], Literal["justify"], Literal["match-parent"], Literal["start"]]] = None,
        lh: typing.Optional[typing.Union[NumberType, Literal["xs"], Literal["sm"], Literal["md"], Literal["lg"], Literal["xl"], Literal["h2"], Literal["h1"], Literal["h3"], Literal["h4"], Literal["h5"], Literal["h6"]]] = None,
        fs: typing.Optional[typing.Union[Literal["-moz-initial"], Literal["inherit"], Literal["initial"], Literal["revert"], Literal["revert-layer"], Literal["unset"], Literal["normal"], Literal["italic"], Literal["oblique"]]] = None,
        tt: typing.Optional[typing.Union[Literal["-moz-initial"], Literal["inherit"], Literal["initial"], Literal["revert"], Literal["revert-layer"], Literal["unset"], Literal["none"], Literal["capitalize"], Literal["full-size-kana"], Literal["full-width"], Literal["lowercase"], Literal["uppercase"]]] = None,
        td: typing.Optional[typing.Union[str, NumberType]] = None,
        w: typing.Optional[typing.Union[str, NumberType]] = None,
        miw: typing.Optional[typing.Union[str, NumberType]] = None,
        maw: typing.Optional[typing.Union[str, NumberType]] = None,
        h: typing.Optional[typing.Union[str, NumberType]] = None,
        mih: typing.Optional[typing.Union[str, NumberType]] = None,
        mah: typing.Optional[typing.Union[str, NumberType]] = None,
        bgsz: typing.Optional[typing.Union[str, NumberType]] = None,
        bgp: typing.Optional[typing.Union[str, NumberType]] = None,
        bgr: typing.Optional[typing.Union[Literal["-moz-initial"], Literal["inherit"], Literal["initial"], Literal["revert"], Literal["revert-layer"], Literal["unset"], Literal["no-repeat"], Literal["repeat"], Literal["repeat-x"], Literal["repeat-y"], Literal["round"], Literal["space"]]] = None,
        bga: typing.Optional[typing.Union[Literal["-moz-initial"], Literal["inherit"], Literal["initial"], Literal["revert"], Literal["revert-layer"], Literal["unset"], Literal["fixed"], Literal["local"], Literal["scroll"]]] = None,
        pos: typing.Optional[typing.Union[Literal["-moz-initial"], Literal["inherit"], Literal["initial"], Literal["revert"], Literal["revert-layer"], Literal["unset"], Literal["fixed"], Literal["-webkit-sticky"], Literal["absolute"], Literal["relative"], Literal["static"], Literal["sticky"]]] = None,
        top: typing.Optional[typing.Union[str, NumberType]] = None,
        left: typing.Optional[typing.Union[str, NumberType]] = None,
        bottom: typing.Optional[typing.Union[str, NumberType]] = None,
        right: typing.Optional[typing.Union[str, NumberType]] = None,
        inset: typing.Optional[typing.Union[str, NumberType]] = None,
        display: typing.Optional[typing.Union[Literal["flex"], Literal["-moz-initial"], Literal["inherit"], Literal["initial"], Literal["revert"], Literal["revert-layer"], Literal["unset"], Literal["none"], Literal["block"], Literal["inline"], Literal["run-in"], Literal["-ms-flexbox"], Literal["-ms-grid"], Literal["-webkit-flex"], Literal["flow"], Literal["flow-root"], Literal["grid"], Literal["ruby"], Literal["table"], Literal["ruby-base"], Literal["ruby-base-container"], Literal["ruby-text"], Literal["ruby-text-container"], Literal["table-caption"], Literal["table-cell"], Literal["table-column"], Literal["table-column-group"], Literal["table-footer-group"], Literal["table-header-group"], Literal["table-row"], Literal["table-row-group"], Literal["-ms-inline-flexbox"], Literal["-ms-inline-grid"], Literal["-webkit-inline-flex"], Literal["inline-block"], Literal["inline-flex"], Literal["inline-grid"], Literal["inline-list-item"], Literal["inline-table"], Literal["contents"], Literal["list-item"]]] = None,
        flex: typing.Optional[typing.Union[str, NumberType]] = None,
        dataKey: typing.Optional[str] = None,
        referenceLines: typing.Optional[typing.Sequence[dict]] = None,
        withXAxis: typing.Optional[bool] = None,
        withYAxis: typing.Optional[bool] = None,
        xAxisProps: typing.Optional[dict] = None,
        yAxisProps: typing.Optional[dict] = None,
        gridProps: typing.Optional[dict] = None,
        tickLine: typing.Optional[Literal["none", "x", "y", "xy"]] = None,
        strokeDasharray: typing.Optional[typing.Union[str, NumberType]] = None,
        gridAxis: typing.Optional[Literal["none", "x", "y", "xy"]] = None,
        unit: typing.Optional[str] = None,
        tooltipAnimationDuration: typing.Optional[NumberType] = None,
        legendProps: typing.Optional[dict] = None,
        tooltipProps: typing.Optional[dict] = None,
        withLegend: typing.Optional[bool] = None,
        withTooltip: typing.Optional[bool] = None,
        textColor: typing.Optional[typing.Union[Literal["dark"], Literal["gray"], Literal["red"], Literal["pink"], Literal["grape"], Literal["violet"], Literal["indigo"], Literal["blue"], Literal["cyan"], Literal["green"], Literal["lime"], Literal["yellow"], Literal["orange"], Literal["teal"]]] = None,
        gridColor: typing.Optional[typing.Union[Literal["dark"], Literal["gray"], Literal["red"], Literal["pink"], Literal["grape"], Literal["violet"], Literal["indigo"], Literal["blue"], Literal["cyan"], Literal["green"], Literal["lime"], Literal["yellow"], Literal["orange"], Literal["teal"]]] = None,
        orientation: typing.Optional[Literal["horizontal", "vertical"]] = None,
        xAxisLabel: typing.Optional[str] = None,
        yAxisLabel: typing.Optional[str] = None,
        withRightYAxis: typing.Optional[bool] = None,
        rightYAxisProps: typing.Optional[typing.Any] = None,
        rightYAxisLabel: typing.Optional[typing.Any] = None,
        valueFormatter: typing.Optional[typing.Any] = None,
        classNames: typing.Optional[dict] = None,
        styles: typing.Optional[typing.Any] = None,
        unstyled: typing.Optional[bool] = None,
        variant: typing.Optional[str] = None,
        id: typing.Optional[typing.Union[str, dict]] = None,
        tabIndex: typing.Optional[NumberType] = None,
        loading_state: typing.Optional["LoadingState"] = None,
        **kwargs
    ):
        self._prop_names = ['children', 'id', 'activeDotProps', 'aria-*', 'bd', 'bg', 'bga', 'bgp', 'bgr', 'bgsz', 'bottom', 'c', 'className', 'classNames', 'clickData', 'clickSeriesName', 'connectNulls', 'curveType', 'darkHidden', 'data', 'data-*', 'dataKey', 'display', 'dotProps', 'ff', 'fillOpacity', 'flex', 'fs', 'fw', 'fz', 'gradientStops', 'gridAxis', 'gridColor', 'gridProps', 'h', 'hiddenFrom', 'highlightHover', 'hoverData', 'hoverSeriesName', 'inset', 'left', 'legendProps', 'lh', 'lightHidden', 'lineChartProps', 'lineProps', 'loading_state', 'lts', 'm', 'mah', 'maw', 'mb', 'me', 'mih', 'miw', 'ml', 'mod', 'mr', 'ms', 'mt', 'mx', 'my', 'opacity', 'orientation', 'p', 'pb', 'pe', 'pl', 'pos', 'pr', 'ps', 'pt', 'px', 'py', 'referenceLines', 'right', 'rightYAxisLabel', 'rightYAxisProps', 'series', 'strokeDasharray', 'strokeWidth', 'style', 'styles', 'ta', 'tabIndex', 'td', 'textColor', 'tickLine', 'tooltipAnimationDuration', 'tooltipProps', 'top', 'tt', 'type', 'unit', 'unstyled', 'valueFormatter', 'variant', 'visibleFrom', 'w', 'withDots', 'withLegend', 'withPointLabels', 'withRightYAxis', 'withTooltip', 'withXAxis', 'withYAxis', 'xAxisLabel', 'xAxisProps', 'yAxisLabel', 'yAxisProps']
        self._valid_wildcard_attributes =            ['data-', 'aria-']
        self.available_properties = ['children', 'id', 'activeDotProps', 'aria-*', 'bd', 'bg', 'bga', 'bgp', 'bgr', 'bgsz', 'bottom', 'c', 'className', 'classNames', 'clickData', 'clickSeriesName', 'connectNulls', 'curveType', 'darkHidden', 'data', 'data-*', 'dataKey', 'display', 'dotProps', 'ff', 'fillOpacity', 'flex', 'fs', 'fw', 'fz', 'gradientStops', 'gridAxis', 'gridColor', 'gridProps', 'h', 'hiddenFrom', 'highlightHover', 'hoverData', 'hoverSeriesName', 'inset', 'left', 'legendProps', 'lh', 'lightHidden', 'lineChartProps', 'lineProps', 'loading_state', 'lts', 'm', 'mah', 'maw', 'mb', 'me', 'mih', 'miw', 'ml', 'mod', 'mr', 'ms', 'mt', 'mx', 'my', 'opacity', 'orientation', 'p', 'pb', 'pe', 'pl', 'pos', 'pr', 'ps', 'pt', 'px', 'py', 'referenceLines', 'right', 'rightYAxisLabel', 'rightYAxisProps', 'series', 'strokeDasharray', 'strokeWidth', 'style', 'styles', 'ta', 'tabIndex', 'td', 'textColor', 'tickLine', 'tooltipAnimationDuration', 'tooltipProps', 'top', 'tt', 'type', 'unit', 'unstyled', 'valueFormatter', 'variant', 'visibleFrom', 'w', 'withDots', 'withLegend', 'withPointLabels', 'withRightYAxis', 'withTooltip', 'withXAxis', 'withYAxis', 'xAxisLabel', 'xAxisProps', 'yAxisLabel', 'yAxisProps']
        self.available_wildcard_properties =            ['data-', 'aria-']
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in ['data', 'dataKey', 'series']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(LineChart, self).__init__(children=children, **args)

setattr(LineChart, "__init__", _explicitize_args(LineChart.__init__))
