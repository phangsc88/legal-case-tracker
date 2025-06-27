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


class NumberInput(Component):
    """A NumberInput component.
The NumberInput component allows users to input numeric values 

Keyword arguments:

- id (string; optional):
    Unique ID to identify this component in Dash callbacks.

- allowDecimal (boolean; optional):
    Determines whether decimal values are allowed, `True` by default.

- allowLeadingZeros (boolean; optional):
    Determines whether leading zeros are allowed. If not set, leading
    zeros are removed when the input is blurred. `False` by default.

- allowNegative (boolean; optional):
    Determines whether negative values are allowed, `True` by default.

- allowedDecimalSeparators (list of strings; optional):
    Characters which when pressed result in a decimal separator,
    `['.']` by default.

- aria-* (string; optional):
    Wild card aria attributes.

- autoComplete (string; default 'off'):
    (string; default \"off\") Enables the browser to attempt
    autocompletion based on user history.  For more information, see:
    https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes/autocomplete.

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

- clampBehavior (a value equal to: 'none', 'strict', 'blur'; optional):
    Controls how value is clamped, `strict` – user is not allowed to
    enter values that are not in `[min, max]` range, `blur` – user is
    allowed to enter any values, but the value is clamped when the
    input loses focus (default behavior), `none` – lifts all
    restrictions, `[min, max]` range is applied only for controls and
    up/down keys.

- className (string; optional):
    Class added to the root element, if applicable.

- classNames (dict; optional):
    Adds class names to Mantine components.

- darkHidden (boolean; optional):
    Determines whether component should be hidden in dark color scheme
    with `display: none`.

- data-* (string; optional):
    Wild card data attributes.

- debounce (number; default False):
    (boolean | number; default False): If True, changes to input will
    be sent back to the Dash server only on enter or when losing
    focus. If it's False, it will send the value back on every change.
    If a number, it will not send anything back to the Dash server
    until the user has stopped typing for that number of milliseconds.

- decimalScale (number; optional):
    Limits the number of digits that can be entered after the decimal
    point.

- decimalSeparator (string; optional):
    Character used as a decimal separator, `'.'` by default.

- description (a list of or a singular dash component, string or number; optional):
    Contents of `Input.Description` component. If not set, description
    is not rendered.

- descriptionProps (dict with strings as keys and values of type boolean | number | string | dict | list; optional):
    Props passed down to the `Input.Description` component.

- disabled (boolean; optional):
    Sets disabled attribute on the input element.

- display (optional)

- error (a list of or a singular dash component, string or number; optional):
    Contents of `Input.Error` component. If not set, error is not
    rendered.

- errorProps (dict with strings as keys and values of type boolean | number | string | dict | list; optional):
    Props passed down to the `Input.Error` component.

- ff (optional):
    FontFamily.

- fixedDecimalScale (boolean; optional):
    If set, 0s are added after `decimalSeparator` to match given
    `decimalScale`. `False` by default.

- flex (string | number; optional)

- fs (optional):
    FontStyle.

- fw (optional):
    FontWeight.

- fz (number; optional):
    FontSize, theme key: theme.fontSizes.

- h (string | number; optional):
    Height, theme key: theme.spacing.

- hiddenFrom (optional):
    Breakpoint above which the component is hidden with `display:
    none`.

- hideControls (boolean; optional):
    Determines whether the up/down controls should be hidden, `False`
    by default.

- inputProps (dict with strings as keys and values of type boolean | number | string | dict | list; optional):
    Props passed down to the `Input` component.

- inputWrapperOrder (list of a value equal to: 'label', 'input', 'description', 'error's; optional):
    Controls order of the elements, `['label', 'description', 'input',
    'error']` by default.

- inset (string | number; optional)

- label (a list of or a singular dash component, string or number; optional):
    Contents of `Input.Label` component. If not set, label is not
    rendered.

- labelProps (dict with strings as keys and values of type boolean | number | string | dict | list; optional):
    Props passed down to the `Input.Label` component.

- left (string | number; optional)

- leftSection (a list of or a singular dash component, string or number; optional):
    Content section rendered on the left side of the input.

- leftSectionPointerEvents (a value equal to: '-moz-initial', 'inherit', 'initial', 'revert', 'revert-layer', 'unset', 'none', 'auto', 'all', 'fill', 'painted', 'stroke', 'visible', 'visibleFill', 'visiblePainted', 'visibleStroke'; optional):
    Sets `pointer-events` styles on the `leftSection` element,
    `'none'` by default.

- leftSectionProps (dict; optional):
    Props passed down to the `leftSection` element.

- leftSectionWidth (string | number; optional):
    Left section width, used to set `width` of the section and input
    `padding-left`, by default equals to the input height.

- lh (number; optional):
    LineHeight, theme key: lineHeights.

- lightHidden (boolean; optional):
    Determines whether component should be hidden in light color
    scheme with `display: none`.

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

- max (number; optional):
    Maximum possible value.

- mb (number; optional):
    MarginBottom, theme key: theme.spacing.

- me (number; optional):
    MarginInlineEnd, theme key: theme.spacing.

- mih (string | number; optional):
    MinHeight, theme key: theme.spacing.

- min (number; optional):
    Minimum possible value.

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

- n_blur (number; default 0):
    An integer that represents the number of times that this element
    has lost focus.

- n_submit (number; default 0):
    An integer that represents the number of times that this element
    has been submitted.

- name (string; optional):
    Name prop.

- opacity (optional)

- p (number; optional):
    Padding, theme key: theme.spacing.

- pb (number; optional):
    PaddingBottom, theme key: theme.spacing.

- pe (number; optional):
    PaddingInlineEnd, theme key: theme.spacing.

- persisted_props (list of strings; optional):
    Properties whose user interactions will persist after refreshing
    the component or the page. Since only `value` is allowed this prop
    can normally be ignored.

- persistence (string | number; optional):
    Used to allow user interactions in this component to be persisted
    when the component - or the page - is refreshed. If `persisted` is
    truthy and hasn't changed from its previous value, a `value` that
    the user has changed while using the app will keep that change, as
    long as the new `value` also matches what was given originally.
    Used in conjunction with `persistence_type`.

- persistence_type (a value equal to: 'local', 'session', 'memory'; optional):
    Where persisted user changes will be stored: memory: only kept in
    memory, reset on page refresh. local: window.localStorage, data is
    kept after the browser quit. session: window.sessionStorage, data
    is cleared once the browser quit.

- pl (number; optional):
    PaddingLeft, theme key: theme.spacing.

- placeholder (string; optional):
    Placeholder.

- pointer (boolean; optional):
    Determines whether the input should have `cursor: pointer` style,
    `False` by default.

- pos (optional):
    Position.

- pr (number; optional):
    PaddingRight, theme key: theme.spacing.

- prefix (string; optional):
    Prefix added before the input value.

- ps (number; optional):
    PaddingInlineStart, theme key: theme.spacing.

- pt (number; optional):
    PaddingTop, theme key: theme.spacing.

- px (number; optional):
    PaddingInline, theme key: theme.spacing.

- py (number; optional):
    PaddingBlock, theme key: theme.spacing.

- radius (number; optional):
    Key of `theme.radius` or any valid CSS value to set
    `border-radius`, numbers are converted to rem,
    `theme.defaultRadius` by default.

- readOnly (boolean; optional):
    Readonly.

- required (boolean; optional):
    Adds required attribute to the input and a red asterisk on the
    right side of label, `False` by default.

- right (string | number; optional)

- rightSection (a list of or a singular dash component, string or number; optional):
    Content section rendered on the right side of the input.

- rightSectionPointerEvents (a value equal to: '-moz-initial', 'inherit', 'initial', 'revert', 'revert-layer', 'unset', 'none', 'auto', 'all', 'fill', 'painted', 'stroke', 'visible', 'visibleFill', 'visiblePainted', 'visibleStroke'; optional):
    Sets `pointer-events` styles on the `rightSection` element,
    `'none'` by default.

- rightSectionProps (dict; optional):
    Props passed down to the `rightSection` element.

- rightSectionWidth (string | number; optional):
    Right section width, used to set `width` of the section and input
    `padding-right`, by default equals to the input height.

- size (optional):
    Controls input `height` and horizontal `padding`, `'sm'` by
    default.

- startValue (number; optional):
    Value set to the input when increment/decrement buttons are
    clicked or up/down arrows pressed if the input is empty, `0` by
    default.

- step (number; optional):
    Number by which value will be incremented/decremented with up/down
    controls and keyboard arrows, `1` by default.

- stepHoldDelay (number; optional):
    Initial delay in milliseconds before stepping the value.

- stepHoldInterval (number; optional):
    Delay before stepping the value. Can be a number of milliseconds
    or a function that receives the current step count and returns the
    delay in milliseconds.

- styles (boolean | number | string | dict | list; optional):
    Mantine styles API.

- suffix (string; optional):
    Suffix added after the input value.

- ta (optional):
    TextAlign.

- tabIndex (number; optional):
    tab-index.

- td (string | number; optional):
    TextDecoration.

- thousandSeparator (string; optional):
    A character used to separate thousands.

- thousandsGroupStyle (a value equal to: 'none', 'thousand', 'lakh', 'wan'; optional):
    Defines the thousand grouping style.

- top (string | number; optional)

- tt (optional):
    TextTransform.

- type (a value equal to: 'text', 'tel', 'password'; optional):
    Controls input `type` attribute, `'text'` by default.

- unstyled (boolean; optional):
    Remove all Mantine styling from the component.

- value (string | number; optional):
    Controlled component value.

- valueIsNumericString (boolean; optional):
    If value is passed as string representation of numbers
    (unformatted) and number is used in any format props like in
    prefix or suffix in numeric format and format prop in pattern
    format then this should be passed as `True`. `False` by default.

- variant (string; optional):
    variant.

- visibleFrom (optional):
    Breakpoint below which the component is hidden with `display:
    none`.

- w (string | number; optional):
    Width, theme key: theme.spacing.

- withAsterisk (boolean; optional):
    Determines whether the required asterisk should be displayed.
    Overrides `required` prop. Does not add required attribute to the
    input. `False` by default.

- withErrorStyles (boolean; optional):
    Determines whether the input should have red border and red text
    color when the `error` prop is set, `True` by default.

- wrapperProps (dict with strings as keys and values of type boolean | number | string | dict | list; optional):
    Props passed down to the root element."""
    _children_props = ['label', 'description', 'error', 'leftSection', 'rightSection']
    _base_nodes = ['label', 'description', 'error', 'leftSection', 'rightSection', 'children']
    _namespace = 'dash_mantine_components'
    _type = 'NumberInput'
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
        value: typing.Optional[typing.Union[str, NumberType]] = None,
        allowLeadingZeros: typing.Optional[bool] = None,
        allowNegative: typing.Optional[bool] = None,
        allowedDecimalSeparators: typing.Optional[typing.Sequence[str]] = None,
        decimalScale: typing.Optional[NumberType] = None,
        decimalSeparator: typing.Optional[str] = None,
        fixedDecimalScale: typing.Optional[bool] = None,
        prefix: typing.Optional[str] = None,
        suffix: typing.Optional[str] = None,
        thousandsGroupStyle: typing.Optional[Literal["none", "thousand", "lakh", "wan"]] = None,
        valueIsNumericString: typing.Optional[bool] = None,
        type: typing.Optional[Literal["text", "tel", "password"]] = None,
        thousandSeparator: typing.Optional[typing.Union[str]] = None,
        min: typing.Optional[NumberType] = None,
        max: typing.Optional[NumberType] = None,
        step: typing.Optional[NumberType] = None,
        hideControls: typing.Optional[bool] = None,
        clampBehavior: typing.Optional[Literal["none", "strict", "blur"]] = None,
        allowDecimal: typing.Optional[bool] = None,
        startValue: typing.Optional[NumberType] = None,
        stepHoldInterval: typing.Optional[typing.Union[NumberType, typing.Any]] = None,
        stepHoldDelay: typing.Optional[NumberType] = None,
        autoComplete: typing.Optional[str] = None,
        disabled: typing.Optional[bool] = None,
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
        bg: typing.Optional[typing.Union[Literal["blue"], Literal["cyan"], Literal["gray"], Literal["green"], Literal["indigo"], Literal["lime"], Literal["orange"], Literal["pink"], Literal["red"], Literal["teal"], Literal["violet"], Literal["yellow"], Literal["dark"], Literal["grape"]]] = None,
        c: typing.Optional[typing.Union[Literal["blue"], Literal["cyan"], Literal["gray"], Literal["green"], Literal["indigo"], Literal["lime"], Literal["orange"], Literal["pink"], Literal["red"], Literal["teal"], Literal["violet"], Literal["yellow"], Literal["dark"], Literal["grape"]]] = None,
        opacity: typing.Optional[typing.Union[Literal["-moz-initial"], Literal["inherit"], Literal["initial"], Literal["revert"], Literal["revert-layer"], Literal["unset"]]] = None,
        ff: typing.Optional[typing.Union[Literal["monospace"], Literal["text"], Literal["heading"]]] = None,
        fz: typing.Optional[typing.Union[NumberType, Literal["xs"], Literal["sm"], Literal["md"], Literal["lg"], Literal["xl"], Literal["h1"], Literal["h2"], Literal["h3"], Literal["h4"], Literal["h5"], Literal["h6"]]] = None,
        fw: typing.Optional[typing.Union[Literal["-moz-initial"], Literal["inherit"], Literal["initial"], Literal["revert"], Literal["revert-layer"], Literal["unset"], Literal["bold"], Literal["normal"], Literal["bolder"], Literal["lighter"]]] = None,
        lts: typing.Optional[typing.Union[str, NumberType]] = None,
        ta: typing.Optional[typing.Union[Literal["left"], Literal["right"], Literal["-moz-initial"], Literal["inherit"], Literal["initial"], Literal["revert"], Literal["revert-layer"], Literal["unset"], Literal["-webkit-match-parent"], Literal["center"], Literal["end"], Literal["justify"], Literal["match-parent"], Literal["start"]]] = None,
        lh: typing.Optional[typing.Union[NumberType, Literal["xs"], Literal["sm"], Literal["md"], Literal["lg"], Literal["xl"], Literal["h1"], Literal["h2"], Literal["h3"], Literal["h4"], Literal["h5"], Literal["h6"]]] = None,
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
        wrapperProps: typing.Optional[typing.Dict[typing.Union[str, float, int], typing.Any]] = None,
        readOnly: typing.Optional[bool] = None,
        label: typing.Optional[ComponentType] = None,
        description: typing.Optional[ComponentType] = None,
        error: typing.Optional[ComponentType] = None,
        required: typing.Optional[bool] = None,
        withAsterisk: typing.Optional[bool] = None,
        labelProps: typing.Optional[typing.Dict[typing.Union[str, float, int], typing.Any]] = None,
        descriptionProps: typing.Optional[typing.Dict[typing.Union[str, float, int], typing.Any]] = None,
        errorProps: typing.Optional[typing.Dict[typing.Union[str, float, int], typing.Any]] = None,
        inputWrapperOrder: typing.Optional[typing.Sequence[Literal["label", "input", "description", "error"]]] = None,
        leftSection: typing.Optional[ComponentType] = None,
        leftSectionWidth: typing.Optional[typing.Union[str, NumberType]] = None,
        leftSectionProps: typing.Optional[dict] = None,
        leftSectionPointerEvents: typing.Optional[Literal["-moz-initial", "inherit", "initial", "revert", "revert-layer", "unset", "none", "auto", "all", "fill", "painted", "stroke", "visible", "visibleFill", "visiblePainted", "visibleStroke"]] = None,
        rightSection: typing.Optional[ComponentType] = None,
        rightSectionWidth: typing.Optional[typing.Union[str, NumberType]] = None,
        rightSectionProps: typing.Optional[dict] = None,
        rightSectionPointerEvents: typing.Optional[Literal["-moz-initial", "inherit", "initial", "revert", "revert-layer", "unset", "none", "auto", "all", "fill", "painted", "stroke", "visible", "visibleFill", "visiblePainted", "visibleStroke"]] = None,
        radius: typing.Optional[typing.Union[NumberType, Literal["xs"], Literal["sm"], Literal["md"], Literal["lg"], Literal["xl"]]] = None,
        size: typing.Optional[typing.Union[Literal["xs"], Literal["sm"], Literal["md"], Literal["lg"], Literal["xl"]]] = None,
        pointer: typing.Optional[bool] = None,
        withErrorStyles: typing.Optional[bool] = None,
        placeholder: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        inputProps: typing.Optional[typing.Dict[typing.Union[str, float, int], typing.Any]] = None,
        classNames: typing.Optional[dict] = None,
        styles: typing.Optional[typing.Any] = None,
        unstyled: typing.Optional[bool] = None,
        variant: typing.Optional[str] = None,
        id: typing.Optional[typing.Union[str, dict]] = None,
        tabIndex: typing.Optional[NumberType] = None,
        loading_state: typing.Optional["LoadingState"] = None,
        n_blur: typing.Optional[NumberType] = None,
        n_submit: typing.Optional[NumberType] = None,
        debounce: typing.Optional[typing.Union[NumberType]] = None,
        persistence: typing.Optional[typing.Union[str, NumberType]] = None,
        persisted_props: typing.Optional[typing.Sequence[str]] = None,
        persistence_type: typing.Optional[Literal["local", "session", "memory"]] = None,
        **kwargs
    ):
        self._prop_names = ['id', 'allowDecimal', 'allowLeadingZeros', 'allowNegative', 'allowedDecimalSeparators', 'aria-*', 'autoComplete', 'bd', 'bg', 'bga', 'bgp', 'bgr', 'bgsz', 'bottom', 'c', 'clampBehavior', 'className', 'classNames', 'darkHidden', 'data-*', 'debounce', 'decimalScale', 'decimalSeparator', 'description', 'descriptionProps', 'disabled', 'display', 'error', 'errorProps', 'ff', 'fixedDecimalScale', 'flex', 'fs', 'fw', 'fz', 'h', 'hiddenFrom', 'hideControls', 'inputProps', 'inputWrapperOrder', 'inset', 'label', 'labelProps', 'left', 'leftSection', 'leftSectionPointerEvents', 'leftSectionProps', 'leftSectionWidth', 'lh', 'lightHidden', 'loading_state', 'lts', 'm', 'mah', 'maw', 'max', 'mb', 'me', 'mih', 'min', 'miw', 'ml', 'mod', 'mr', 'ms', 'mt', 'mx', 'my', 'n_blur', 'n_submit', 'name', 'opacity', 'p', 'pb', 'pe', 'persisted_props', 'persistence', 'persistence_type', 'pl', 'placeholder', 'pointer', 'pos', 'pr', 'prefix', 'ps', 'pt', 'px', 'py', 'radius', 'readOnly', 'required', 'right', 'rightSection', 'rightSectionPointerEvents', 'rightSectionProps', 'rightSectionWidth', 'size', 'startValue', 'step', 'stepHoldDelay', 'stepHoldInterval', 'style', 'styles', 'suffix', 'ta', 'tabIndex', 'td', 'thousandSeparator', 'thousandsGroupStyle', 'top', 'tt', 'type', 'unstyled', 'value', 'valueIsNumericString', 'variant', 'visibleFrom', 'w', 'withAsterisk', 'withErrorStyles', 'wrapperProps']
        self._valid_wildcard_attributes =            ['data-', 'aria-']
        self.available_properties = ['id', 'allowDecimal', 'allowLeadingZeros', 'allowNegative', 'allowedDecimalSeparators', 'aria-*', 'autoComplete', 'bd', 'bg', 'bga', 'bgp', 'bgr', 'bgsz', 'bottom', 'c', 'clampBehavior', 'className', 'classNames', 'darkHidden', 'data-*', 'debounce', 'decimalScale', 'decimalSeparator', 'description', 'descriptionProps', 'disabled', 'display', 'error', 'errorProps', 'ff', 'fixedDecimalScale', 'flex', 'fs', 'fw', 'fz', 'h', 'hiddenFrom', 'hideControls', 'inputProps', 'inputWrapperOrder', 'inset', 'label', 'labelProps', 'left', 'leftSection', 'leftSectionPointerEvents', 'leftSectionProps', 'leftSectionWidth', 'lh', 'lightHidden', 'loading_state', 'lts', 'm', 'mah', 'maw', 'max', 'mb', 'me', 'mih', 'min', 'miw', 'ml', 'mod', 'mr', 'ms', 'mt', 'mx', 'my', 'n_blur', 'n_submit', 'name', 'opacity', 'p', 'pb', 'pe', 'persisted_props', 'persistence', 'persistence_type', 'pl', 'placeholder', 'pointer', 'pos', 'pr', 'prefix', 'ps', 'pt', 'px', 'py', 'radius', 'readOnly', 'required', 'right', 'rightSection', 'rightSectionPointerEvents', 'rightSectionProps', 'rightSectionWidth', 'size', 'startValue', 'step', 'stepHoldDelay', 'stepHoldInterval', 'style', 'styles', 'suffix', 'ta', 'tabIndex', 'td', 'thousandSeparator', 'thousandsGroupStyle', 'top', 'tt', 'type', 'unstyled', 'value', 'valueIsNumericString', 'variant', 'visibleFrom', 'w', 'withAsterisk', 'withErrorStyles', 'wrapperProps']
        self.available_wildcard_properties =            ['data-', 'aria-']
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(NumberInput, self).__init__(**args)

setattr(NumberInput, "__init__", _explicitize_args(NumberInput.__init__))
