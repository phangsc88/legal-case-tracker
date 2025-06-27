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


class TimePicker(Component):
    """A TimePicker component.
TimePicker

Keyword arguments:

- id (string; optional):
    Unique ID to identify this component in Dash callbacks.

- amPmInputLabel (string; optional):
    `aria-label` of am/pm input.

- amPmLabels (dict; optional):
    Labels used for am/pm values, `{ am: 'AM', pm: 'PM' }` by default.

    `amPmLabels` is a dict with keys:

    - am (string; required)

    - pm (string; required)

- amPmSelectProps (boolean | number | string | dict | list; optional):
    Props passed down to am/pm select.

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

- clearButtonProps (boolean | number | string | dict | list; optional):
    Props passed down to clear button.

- clearable (boolean; optional):
    Determines whether the clear button should be displayed, `False`
    by default.

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

- defaultValue (string; optional):
    Uncontrolled component default value.

- description (a list of or a singular dash component, string or number; optional):
    Contents of `Input.Description` component. If not set, description
    is not rendered.

- descriptionProps (dict with strings as keys and values of type boolean | number | string | dict | list; optional):
    Props passed down to the `Input.Description` component.

- disabled (boolean; optional):
    If set, the component becomes disabled.

- display (optional)

- error (a list of or a singular dash component, string or number; optional):
    Contents of `Input.Error` component. If not set, error is not
    rendered.

- errorProps (dict with strings as keys and values of type boolean | number | string | dict | list; optional):
    Props passed down to the `Input.Error` component.

- ff (optional):
    FontFamily.

- flex (string | number; optional)

- form (string; optional):
    `form` prop passed down to the hidden input.

- format (a value equal to: '12h', '24h'; optional):
    Time format, `'24h'` by default.

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

- hiddenInputProps (boolean | number | string | dict | list; optional):
    Props passed down to the hidden input.

- hoursInputLabel (string; optional):
    `aria-label` of hours input.

- hoursInputProps (boolean | number | string | dict | list; optional):
    Props passed down to hours input.

- hoursStep (number; optional):
    Number by which hours are incremented/decremented, `1` by default.

- inputProps (dict with strings as keys and values of type boolean | number | string | dict | list; optional):
    Props passed down to the `Input` component.

- inputWrapperOrder (list of a value equal to: 'label', 'description', 'error', 'input's; optional):
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

- leftSectionPointerEvents (a value equal to: '-moz-initial', 'inherit', 'initial', 'revert', 'revert-layer', 'unset', 'auto', 'none', 'all', 'fill', 'painted', 'stroke', 'visible', 'visibleFill', 'visiblePainted', 'visibleStroke'; optional):
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

- max (string; optional):
    Max possible time value in `hh:mm:ss` format.

- maxDropdownContentHeight (number; optional):
    Maximum height of the content displayed in the dropdown in px,
    `200` by default.

- mb (number; optional):
    MarginBottom, theme key: theme.spacing.

- me (number; optional):
    MarginInlineEnd, theme key: theme.spacing.

- mih (string | number; optional):
    MinHeight, theme key: theme.spacing.

- min (string; optional):
    Min possible time value in `hh:mm:ss` format.

- minutesInputLabel (string; optional):
    `aria-label` of minutes input.

- minutesInputProps (boolean | number | string | dict | list; optional):
    Props passed down to minutes input.

- minutesStep (number; optional):
    Number by which minutes are incremented/decremented, `1` by
    default.

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
    `name` prop passed down to the hidden input.

- opacity (optional)

- p (number; optional):
    Padding, theme key: theme.spacing.

- pasteSplit (dict; optional):
    A function to transform paste values, by default time in 24h
    format can be parsed on paste for example `23:34:22`.

    `pasteSplit` is a dict with keys:


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

- popoverProps (dict; optional):
    Props passed down to `Popover` component.

    `popoverProps` is a dict with keys:

    - children (a list of or a singular dash component, string or number; optional):
        `Popover.Target` and `Popover.Dropdown` components.

    - opened (boolean; optional):
        Controlled dropdown opened state.

    - closeOnClickOutside (boolean; optional):
        Determines whether dropdown should be closed on outside
        clicks, `True` by default.

    - clickOutsideEvents (list of strings; optional):
        Events that trigger outside clicks.

    - trapFocus (boolean; optional):
        Determines whether focus should be trapped within dropdown,
        `False` by default.

    - closeOnEscape (boolean; optional):
        Determines whether dropdown should be closed when `Escape` key
        is pressed, `True` by default.

    - withRoles (boolean; optional):
        Determines whether dropdown and target elements should have
        accessible roles, `True` by default.

    - hideDetached (boolean; optional):
        If set, the dropdown is hidden when the element is hidden with
        styles or not visible on the screen, `True` by default.

    - position (a value equal to: 'top', 'left', 'bottom', 'right', 'top-end', 'top-start', 'left-end', 'left-start', 'bottom-end', 'bottom-start', 'right-end', 'right-start'; optional):
        Dropdown position relative to the target element, `'bottom'`
        by default.

    - offset (number; optional):
        Offset of the dropdown element, `8` by default.

    - positionDependencies (list of boolean | number | string | dict | lists; optional):
        `useEffect` dependencies to force update dropdown position,
        `[]` by default.

    - keepMounted (boolean; optional):
        If set dropdown will not be unmounted from the DOM when it is
        hidden, `display: none` styles will be added instead.

    - transitionProps (dict; optional):
        Props passed down to the `Transition` component that used to
        animate dropdown presence, use to configure duration and
        animation type, `{ duration: 150, transition: 'fade' }` by
        default.

        `transitionProps` is a dict with keys:

        - keepMounted (boolean; optional):
            If set element will not be unmounted from the DOM when it
            is hidden, `display: none` styles will be applied instead.

        - transition (optional):
            Transition name or object.

        - duration (number; optional):
            Transition duration in ms, `250` by default.

        - exitDuration (number; optional):
            Exit transition duration in ms, `250` by default.

        - timingFunction (string; optional):
            Transition timing function,
            `theme.transitionTimingFunction` by default.

        - mounted (boolean; required):
            Determines whether component should be mounted to the DOM.

    - width (string | number; optional):
        Dropdown width, or `'target'` to make dropdown width the same
        as target element, `'max-content'` by default.

    - middlewares (dict; optional):
        Floating ui middlewares to configure position handling, `{
        flip: True, shift: True, inline: False }` by default.

        `middlewares` is a dict with keys:

        - shift (optional)

        - flip (dict; optional)

            `flip` is a dict with keys:

    - mainAxis (boolean; optional):
        The axis that runs along the side of the floating element.
        Determines  whether overflow along this axis is checked to
        perform a flip. @,default,True.

    - crossAxis (boolean; optional):
        The axis that runs along the alignment of the floating
        element. Determines  whether overflow along this axis is
        checked to perform a flip. @,default,True.

    - rootBoundary (dict; optional):
        The root clipping area in which overflow will be checked.
        @,default,'viewport'.

        `rootBoundary` is a dict with keys:

        - x (number; required)

        - y (number; required)

        - width (number; required)

        - height (number; required)

    - elementContext (a value equal to: 'reference', 'floating'; optional):
        The element in which overflow is being checked relative to a
        boundary. @,default,'floating'.

    - altBoundary (boolean; optional):
        Whether to check for overflow using the alternate element's
        boundary  (`clippingAncestors` boundary only).
        @,default,False.

    - padding (dict; optional):
        Virtual padding for the resolved overflow detection offsets.
        @,default,0.

        `padding` is a number

              Or dict with keys:

        - top (number; optional)

        - left (number; optional)

        - bottom (number; optional)

        - right (number; optional)

    - fallbackPlacements (list of a value equal to: 'top', 'left', 'bottom', 'right', 'top-end', 'top-start', 'left-end', 'left-start', 'bottom-end', 'bottom-start', 'right-end', 'right-start's; optional):
        Placements to try sequentially if the preferred `placement`
        does not fit. @,default,[oppositePlacement] (computed).

    - fallbackStrategy (a value equal to: 'bestFit', 'initialPlacement'; optional):
        What strategy to use when no placements fit.
        @,default,'bestFit'.

    - fallbackAxisSideDirection (a value equal to: 'end', 'start', 'none'; optional):
        Whether to allow fallback to the perpendicular axis of the
        preferred  placement, and if so, which side direction along
        the axis to prefer. @,default,'none' (disallow fallback).

    - flipAlignment (boolean; optional):
        Whether to flip to placements with the opposite alignment if
        they fit  better. @,default,True.

    - boundary (dict; optional)

        `boundary` is a dict with keys:

        - x (number; required)

        - y (number; required)

        - width (number; required)

        - height (number; required) | list of a list of or a singular dash component, string or numbers

        - inline (boolean | number | string | dict | list; optional)

        - size (optional)

    - withArrow (boolean; optional):
        Determines whether component should have an arrow, `False` by
        default.

    - arrowSize (number; optional):
        Arrow size in px, `7` by default.

    - arrowOffset (number; optional):
        Arrow offset in px, `5` by default.

    - arrowRadius (number; optional):
        Arrow `border-radius` in px, `0` by default.

    - arrowPosition (a value equal to: 'center', 'side'; optional):
        Arrow position.

    - withinPortal (boolean; optional):
        Determines whether dropdown should be rendered within the
        `Portal`, `True` by default.

    - portalProps (dict; optional):
        Props to pass down to the `Portal` when `withinPortal` is
        True.

    - zIndex (string | number; optional):
        Dropdown `z-index`, `300` by default.

    - radius (number; optional):
        Key of `theme.radius` or any valid CSS value to set
        border-radius, `theme.defaultRadius` by default.

    - shadow (optional):
        Key of `theme.shadows` or any other valid CSS `box-shadow`
        value.

    - disabled (boolean; optional):
        If set, popover dropdown will not be rendered.

    - returnFocus (boolean; optional):
        Determines whether focus should be automatically returned to
        control when dropdown closes, `False` by default.

    - floatingStrategy (a value equal to: 'absolute', 'fixed'; optional):
        Changes floating ui [position
        strategy](https://floating-ui.com/docs/usefloating#strategy),
        `'absolute'` by default.

    - overlayProps (dict; optional):
        Props passed down to `Overlay` component.

    - withOverlay (boolean; optional):
        Determines whether the overlay should be displayed when the
        dropdown is opened, `False` by default.

    - classNames (dict; optional):
        Adds class names to Mantine components.

    - styles (boolean | number | string | dict | list; optional):
        Mantine styles API.

    - unstyled (boolean; optional):
        Remove all Mantine styling from the component.

    - variant (string; optional):
        variant.

- pos (optional):
    Position.

- pr (number; optional):
    PaddingRight, theme key: theme.spacing.

- presets (list of strings; optional):
    Time presets to display in the dropdown.

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
    If set, the value cannot be updated.

- required (boolean; optional):
    Adds required attribute to the input and a red asterisk on the
    right side of label, `False` by default.

- right (string | number; optional)

- rightSection (a list of or a singular dash component, string or number; optional):
    Content section rendered on the right side of the input.

- rightSectionPointerEvents (a value equal to: '-moz-initial', 'inherit', 'initial', 'revert', 'revert-layer', 'unset', 'auto', 'none', 'all', 'fill', 'painted', 'stroke', 'visible', 'visibleFill', 'visiblePainted', 'visibleStroke'; optional):
    Sets `pointer-events` styles on the `rightSection` element,
    `'none'` by default.

- rightSectionProps (dict; optional):
    Props passed down to the `rightSection` element.

- rightSectionWidth (string | number; optional):
    Right section width, used to set `width` of the section and input
    `padding-right`, by default equals to the input height.

- scrollAreaProps (boolean | number | string | dict | list; optional):
    Props passed down to all underlying `ScrollArea` components.

- secondsInputLabel (string; optional):
    `aria-label` of seconds input.

- secondsInputProps (boolean | number | string | dict | list; optional):
    Props passed down to seconds input.

- secondsStep (number; optional):
    Number by which seconds are incremented/decremented, `1` by
    default.

- size (optional):
    Controls input `height` and horizontal `padding`, `'sm'` by
    default.

- styles (boolean | number | string | dict | list; optional):
    Mantine styles API.

- ta (optional):
    TextAlign.

- tabIndex (number; optional):
    tab-index.

- td (string | number; optional):
    TextDecoration.

- timeRangePresets (dict; optional):
    Generates a range of time values for the `presets` prop. Accepts a
    dictionary with `startTime`, `endTime`, and `interval` keys, where
    all values are strings in `hh:mm:ss` format. This overrides any
    values provided directly in the `presets` prop.

    `timeRangePresets` is a dict with keys:

    - startTime (string; required)

    - endTime (string; required)

    - interval (string; required)

- top (string | number; optional)

- tt (optional):
    TextTransform.

- unstyled (boolean; optional):
    Remove all Mantine styling from the component.

- value (string; default ''):
    Value for controlled component.

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

- withDropdown (boolean; optional):
    Determines whether the dropdown with time controls list should be
    visible when the input has focus, `False` by default.

- withErrorStyles (boolean; optional):
    Determines whether the input should have red border and red text
    color when the `error` prop is set, `True` by default.

- withSeconds (boolean; optional):
    Determines whether the seconds input should be displayed, `False`
    by default.

- wrapperProps (dict with strings as keys and values of type boolean | number | string | dict | list; optional):
    Props passed down to the root element."""
    _children_props = ['popoverProps.children', 'popoverProps.middlewares.flip.boundary', 'label', 'description', 'error', 'leftSection', 'rightSection']
    _base_nodes = ['label', 'description', 'error', 'leftSection', 'rightSection', 'children']
    _namespace = 'dash_mantine_components'
    _type = 'TimePicker'
    LoadingState = TypedDict(
        "LoadingState",
            {
            "is_loading": bool,
            "prop_name": str,
            "component_name": str
        }
    )

    AmPmLabels = TypedDict(
        "AmPmLabels",
            {
            "am": str,
            "pm": str
        }
    )

    PopoverPropsTransitionProps = TypedDict(
        "PopoverPropsTransitionProps",
            {
            "keepMounted": NotRequired[bool],
            "transition": NotRequired[typing.Union[Literal["fade"], Literal["fade-down"], Literal["fade-up"], Literal["fade-left"], Literal["fade-right"], Literal["skew-up"], Literal["skew-down"], Literal["rotate-right"], Literal["rotate-left"], Literal["slide-down"], Literal["slide-up"], Literal["slide-right"], Literal["slide-left"], Literal["scale-y"], Literal["scale-x"], Literal["scale"], Literal["pop"], Literal["pop-top-left"], Literal["pop-top-right"], Literal["pop-bottom-left"], Literal["pop-bottom-right"]]],
            "duration": NotRequired[NumberType],
            "exitDuration": NotRequired[NumberType],
            "timingFunction": NotRequired[str],
            "mounted": bool
        }
    )

    PopoverPropsMiddlewaresFlipRootBoundary = TypedDict(
        "PopoverPropsMiddlewaresFlipRootBoundary",
            {
            "x": NumberType,
            "y": NumberType,
            "width": NumberType,
            "height": NumberType
        }
    )

    PopoverPropsMiddlewaresFlipPadding = TypedDict(
        "PopoverPropsMiddlewaresFlipPadding",
            {
            "top": NotRequired[NumberType],
            "left": NotRequired[NumberType],
            "bottom": NotRequired[NumberType],
            "right": NotRequired[NumberType]
        }
    )

    PopoverPropsMiddlewaresFlipBoundary = TypedDict(
        "PopoverPropsMiddlewaresFlipBoundary",
            {
            "x": NumberType,
            "y": NumberType,
            "width": NumberType,
            "height": NumberType
        }
    )

    PopoverPropsMiddlewaresFlip = TypedDict(
        "PopoverPropsMiddlewaresFlip",
            {
            "mainAxis": NotRequired[bool],
            "crossAxis": NotRequired[bool],
            "rootBoundary": NotRequired[typing.Union[Literal["viewport"], Literal["document"], "PopoverPropsMiddlewaresFlipRootBoundary"]],
            "elementContext": NotRequired[Literal["reference", "floating"]],
            "altBoundary": NotRequired[bool],
            "padding": NotRequired[typing.Union[NumberType, "PopoverPropsMiddlewaresFlipPadding"]],
            "fallbackPlacements": NotRequired[typing.Sequence[Literal["top", "left", "bottom", "right", "top-end", "top-start", "left-end", "left-start", "bottom-end", "bottom-start", "right-end", "right-start"]]],
            "fallbackStrategy": NotRequired[Literal["bestFit", "initialPlacement"]],
            "fallbackAxisSideDirection": NotRequired[Literal["end", "start", "none"]],
            "flipAlignment": NotRequired[bool],
            "boundary": NotRequired[typing.Union["PopoverPropsMiddlewaresFlipBoundary", Literal["clippingAncestors"], typing.Sequence[ComponentType]]]
        }
    )

    PopoverPropsMiddlewares = TypedDict(
        "PopoverPropsMiddlewares",
            {
            "shift": NotRequired[typing.Union[typing.Any]],
            "flip": NotRequired[typing.Union["PopoverPropsMiddlewaresFlip"]],
            "inline": NotRequired[typing.Any],
            "size": NotRequired[typing.Union[typing.Any]]
        }
    )

    PopoverProps = TypedDict(
        "PopoverProps",
            {
            "children": NotRequired[ComponentType],
            "opened": NotRequired[bool],
            "closeOnClickOutside": NotRequired[bool],
            "clickOutsideEvents": NotRequired[typing.Sequence[str]],
            "trapFocus": NotRequired[bool],
            "closeOnEscape": NotRequired[bool],
            "withRoles": NotRequired[bool],
            "hideDetached": NotRequired[bool],
            "position": NotRequired[Literal["top", "left", "bottom", "right", "top-end", "top-start", "left-end", "left-start", "bottom-end", "bottom-start", "right-end", "right-start"]],
            "offset": NotRequired[typing.Union[NumberType]],
            "positionDependencies": NotRequired[typing.Sequence[typing.Any]],
            "keepMounted": NotRequired[bool],
            "transitionProps": NotRequired["PopoverPropsTransitionProps"],
            "width": NotRequired[typing.Union[str, NumberType]],
            "middlewares": NotRequired["PopoverPropsMiddlewares"],
            "withArrow": NotRequired[bool],
            "arrowSize": NotRequired[NumberType],
            "arrowOffset": NotRequired[NumberType],
            "arrowRadius": NotRequired[NumberType],
            "arrowPosition": NotRequired[Literal["center", "side"]],
            "withinPortal": NotRequired[bool],
            "portalProps": NotRequired[dict],
            "zIndex": NotRequired[typing.Union[str, NumberType]],
            "radius": NotRequired[typing.Union[NumberType, Literal["xs"], Literal["sm"], Literal["md"], Literal["lg"], Literal["xl"]]],
            "shadow": NotRequired[typing.Union[Literal["xs"], Literal["sm"], Literal["md"], Literal["lg"], Literal["xl"]]],
            "disabled": NotRequired[bool],
            "returnFocus": NotRequired[bool],
            "floatingStrategy": NotRequired[Literal["absolute", "fixed"]],
            "overlayProps": NotRequired[dict],
            "withOverlay": NotRequired[bool],
            "classNames": NotRequired[dict],
            "styles": NotRequired[typing.Any],
            "unstyled": NotRequired[bool],
            "variant": NotRequired[str]
        }
    )

    PasteSplit = TypedDict(
        "PasteSplit",
            {

        }
    )

    TimeRangePresets = TypedDict(
        "TimeRangePresets",
            {
            "startTime": str,
            "endTime": str,
            "interval": str
        }
    )


    def __init__(
        self,
        value: typing.Optional[str] = None,
        id: typing.Optional[typing.Union[str, dict]] = None,
        tabIndex: typing.Optional[NumberType] = None,
        loading_state: typing.Optional["LoadingState"] = None,
        persistence: typing.Optional[typing.Union[str, NumberType]] = None,
        persisted_props: typing.Optional[typing.Sequence[str]] = None,
        persistence_type: typing.Optional[Literal["local", "session", "memory"]] = None,
        n_blur: typing.Optional[NumberType] = None,
        n_submit: typing.Optional[NumberType] = None,
        debounce: typing.Optional[typing.Union[NumberType]] = None,
        defaultValue: typing.Optional[str] = None,
        clearable: typing.Optional[bool] = None,
        name: typing.Optional[str] = None,
        form: typing.Optional[str] = None,
        min: typing.Optional[str] = None,
        max: typing.Optional[str] = None,
        format: typing.Optional[Literal["12h", "24h"]] = None,
        hoursStep: typing.Optional[NumberType] = None,
        minutesStep: typing.Optional[NumberType] = None,
        secondsStep: typing.Optional[NumberType] = None,
        withSeconds: typing.Optional[bool] = None,
        hoursInputLabel: typing.Optional[str] = None,
        minutesInputLabel: typing.Optional[str] = None,
        secondsInputLabel: typing.Optional[str] = None,
        amPmInputLabel: typing.Optional[str] = None,
        amPmLabels: typing.Optional["AmPmLabels"] = None,
        withDropdown: typing.Optional[bool] = None,
        popoverProps: typing.Optional["PopoverProps"] = None,
        clearButtonProps: typing.Optional[typing.Any] = None,
        hoursInputProps: typing.Optional[typing.Any] = None,
        minutesInputProps: typing.Optional[typing.Any] = None,
        secondsInputProps: typing.Optional[typing.Any] = None,
        amPmSelectProps: typing.Optional[typing.Any] = None,
        readOnly: typing.Optional[bool] = None,
        disabled: typing.Optional[bool] = None,
        hiddenInputProps: typing.Optional[typing.Any] = None,
        pasteSplit: typing.Optional["PasteSplit"] = None,
        presets: typing.Optional[typing.Union[typing.Sequence[str]]] = None,
        maxDropdownContentHeight: typing.Optional[NumberType] = None,
        scrollAreaProps: typing.Optional[typing.Any] = None,
        timeRangePresets: typing.Optional["TimeRangePresets"] = None,
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
        ta: typing.Optional[typing.Union[Literal["left"], Literal["right"], Literal["end"], Literal["start"], Literal["-moz-initial"], Literal["inherit"], Literal["initial"], Literal["revert"], Literal["revert-layer"], Literal["unset"], Literal["center"], Literal["-webkit-match-parent"], Literal["justify"], Literal["match-parent"]]] = None,
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
        bga: typing.Optional[typing.Union[Literal["local"], Literal["-moz-initial"], Literal["inherit"], Literal["initial"], Literal["revert"], Literal["revert-layer"], Literal["unset"], Literal["fixed"], Literal["scroll"]]] = None,
        pos: typing.Optional[typing.Union[Literal["-moz-initial"], Literal["inherit"], Literal["initial"], Literal["revert"], Literal["revert-layer"], Literal["unset"], Literal["absolute"], Literal["fixed"], Literal["-webkit-sticky"], Literal["relative"], Literal["static"], Literal["sticky"]]] = None,
        top: typing.Optional[typing.Union[str, NumberType]] = None,
        left: typing.Optional[typing.Union[str, NumberType]] = None,
        bottom: typing.Optional[typing.Union[str, NumberType]] = None,
        right: typing.Optional[typing.Union[str, NumberType]] = None,
        inset: typing.Optional[typing.Union[str, NumberType]] = None,
        display: typing.Optional[typing.Union[Literal["flex"], Literal["-moz-initial"], Literal["inherit"], Literal["initial"], Literal["revert"], Literal["revert-layer"], Literal["unset"], Literal["none"], Literal["block"], Literal["inline"], Literal["run-in"], Literal["-ms-flexbox"], Literal["-ms-grid"], Literal["-webkit-flex"], Literal["flow"], Literal["flow-root"], Literal["grid"], Literal["ruby"], Literal["table"], Literal["ruby-base"], Literal["ruby-base-container"], Literal["ruby-text"], Literal["ruby-text-container"], Literal["table-caption"], Literal["table-cell"], Literal["table-column"], Literal["table-column-group"], Literal["table-footer-group"], Literal["table-header-group"], Literal["table-row"], Literal["table-row-group"], Literal["-ms-inline-flexbox"], Literal["-ms-inline-grid"], Literal["-webkit-inline-flex"], Literal["inline-block"], Literal["inline-flex"], Literal["inline-grid"], Literal["inline-list-item"], Literal["inline-table"], Literal["contents"], Literal["list-item"]]] = None,
        flex: typing.Optional[typing.Union[str, NumberType]] = None,
        wrapperProps: typing.Optional[typing.Dict[typing.Union[str, float, int], typing.Any]] = None,
        label: typing.Optional[ComponentType] = None,
        description: typing.Optional[ComponentType] = None,
        error: typing.Optional[ComponentType] = None,
        required: typing.Optional[bool] = None,
        withAsterisk: typing.Optional[bool] = None,
        labelProps: typing.Optional[typing.Dict[typing.Union[str, float, int], typing.Any]] = None,
        descriptionProps: typing.Optional[typing.Dict[typing.Union[str, float, int], typing.Any]] = None,
        errorProps: typing.Optional[typing.Dict[typing.Union[str, float, int], typing.Any]] = None,
        inputWrapperOrder: typing.Optional[typing.Sequence[Literal["label", "description", "error", "input"]]] = None,
        size: typing.Optional[typing.Union[Literal["xs"], Literal["sm"], Literal["md"], Literal["lg"], Literal["xl"]]] = None,
        leftSection: typing.Optional[ComponentType] = None,
        leftSectionWidth: typing.Optional[typing.Union[str, NumberType]] = None,
        leftSectionProps: typing.Optional[dict] = None,
        leftSectionPointerEvents: typing.Optional[Literal["-moz-initial", "inherit", "initial", "revert", "revert-layer", "unset", "auto", "none", "all", "fill", "painted", "stroke", "visible", "visibleFill", "visiblePainted", "visibleStroke"]] = None,
        rightSection: typing.Optional[ComponentType] = None,
        rightSectionWidth: typing.Optional[typing.Union[str, NumberType]] = None,
        rightSectionProps: typing.Optional[dict] = None,
        rightSectionPointerEvents: typing.Optional[Literal["-moz-initial", "inherit", "initial", "revert", "revert-layer", "unset", "auto", "none", "all", "fill", "painted", "stroke", "visible", "visibleFill", "visiblePainted", "visibleStroke"]] = None,
        radius: typing.Optional[typing.Union[NumberType, Literal["xs"], Literal["sm"], Literal["md"], Literal["lg"], Literal["xl"]]] = None,
        pointer: typing.Optional[bool] = None,
        withErrorStyles: typing.Optional[bool] = None,
        placeholder: typing.Optional[str] = None,
        inputProps: typing.Optional[typing.Dict[typing.Union[str, float, int], typing.Any]] = None,
        classNames: typing.Optional[dict] = None,
        styles: typing.Optional[typing.Any] = None,
        unstyled: typing.Optional[bool] = None,
        variant: typing.Optional[str] = None,
        **kwargs
    ):
        self._prop_names = ['id', 'amPmInputLabel', 'amPmLabels', 'amPmSelectProps', 'aria-*', 'bd', 'bg', 'bga', 'bgp', 'bgr', 'bgsz', 'bottom', 'c', 'className', 'classNames', 'clearButtonProps', 'clearable', 'darkHidden', 'data-*', 'debounce', 'defaultValue', 'description', 'descriptionProps', 'disabled', 'display', 'error', 'errorProps', 'ff', 'flex', 'form', 'format', 'fs', 'fw', 'fz', 'h', 'hiddenFrom', 'hiddenInputProps', 'hoursInputLabel', 'hoursInputProps', 'hoursStep', 'inputProps', 'inputWrapperOrder', 'inset', 'label', 'labelProps', 'left', 'leftSection', 'leftSectionPointerEvents', 'leftSectionProps', 'leftSectionWidth', 'lh', 'lightHidden', 'loading_state', 'lts', 'm', 'mah', 'maw', 'max', 'maxDropdownContentHeight', 'mb', 'me', 'mih', 'min', 'minutesInputLabel', 'minutesInputProps', 'minutesStep', 'miw', 'ml', 'mod', 'mr', 'ms', 'mt', 'mx', 'my', 'n_blur', 'n_submit', 'name', 'opacity', 'p', 'pasteSplit', 'pb', 'pe', 'persisted_props', 'persistence', 'persistence_type', 'pl', 'placeholder', 'pointer', 'popoverProps', 'pos', 'pr', 'presets', 'ps', 'pt', 'px', 'py', 'radius', 'readOnly', 'required', 'right', 'rightSection', 'rightSectionPointerEvents', 'rightSectionProps', 'rightSectionWidth', 'scrollAreaProps', 'secondsInputLabel', 'secondsInputProps', 'secondsStep', 'size', 'style', 'styles', 'ta', 'tabIndex', 'td', 'timeRangePresets', 'top', 'tt', 'unstyled', 'value', 'variant', 'visibleFrom', 'w', 'withAsterisk', 'withDropdown', 'withErrorStyles', 'withSeconds', 'wrapperProps']
        self._valid_wildcard_attributes =            ['data-', 'aria-']
        self.available_properties = ['id', 'amPmInputLabel', 'amPmLabels', 'amPmSelectProps', 'aria-*', 'bd', 'bg', 'bga', 'bgp', 'bgr', 'bgsz', 'bottom', 'c', 'className', 'classNames', 'clearButtonProps', 'clearable', 'darkHidden', 'data-*', 'debounce', 'defaultValue', 'description', 'descriptionProps', 'disabled', 'display', 'error', 'errorProps', 'ff', 'flex', 'form', 'format', 'fs', 'fw', 'fz', 'h', 'hiddenFrom', 'hiddenInputProps', 'hoursInputLabel', 'hoursInputProps', 'hoursStep', 'inputProps', 'inputWrapperOrder', 'inset', 'label', 'labelProps', 'left', 'leftSection', 'leftSectionPointerEvents', 'leftSectionProps', 'leftSectionWidth', 'lh', 'lightHidden', 'loading_state', 'lts', 'm', 'mah', 'maw', 'max', 'maxDropdownContentHeight', 'mb', 'me', 'mih', 'min', 'minutesInputLabel', 'minutesInputProps', 'minutesStep', 'miw', 'ml', 'mod', 'mr', 'ms', 'mt', 'mx', 'my', 'n_blur', 'n_submit', 'name', 'opacity', 'p', 'pasteSplit', 'pb', 'pe', 'persisted_props', 'persistence', 'persistence_type', 'pl', 'placeholder', 'pointer', 'popoverProps', 'pos', 'pr', 'presets', 'ps', 'pt', 'px', 'py', 'radius', 'readOnly', 'required', 'right', 'rightSection', 'rightSectionPointerEvents', 'rightSectionProps', 'rightSectionWidth', 'scrollAreaProps', 'secondsInputLabel', 'secondsInputProps', 'secondsStep', 'size', 'style', 'styles', 'ta', 'tabIndex', 'td', 'timeRangePresets', 'top', 'tt', 'unstyled', 'value', 'variant', 'visibleFrom', 'w', 'withAsterisk', 'withDropdown', 'withErrorStyles', 'withSeconds', 'wrapperProps']
        self.available_wildcard_properties =            ['data-', 'aria-']
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(TimePicker, self).__init__(**args)

setattr(TimePicker, "__init__", _explicitize_args(TimePicker.__init__))
