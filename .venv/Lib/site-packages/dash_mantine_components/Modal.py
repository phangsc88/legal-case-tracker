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


class Modal(Component):
    """A Modal component.
Modal

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    Modal content.

- id (string; optional):
    Unique ID to identify this component in Dash callbacks.

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

- centered (boolean; optional):
    Determines whether the modal should be centered vertically,
    `False` by default.

- className (string; optional):
    Class added to the root element, if applicable.

- classNames (dict; optional):
    Adds class names to Mantine components.

- closeButtonProps (dict; optional):
    Props passed down to the close button.

    `closeButtonProps` is a dict with keys:

    - size (number; optional):
        Controls width and height of the button. Numbers are converted
        to rem. `'md'` by default.

    - radius (number; optional):
        Key of `theme.radius` or any valid CSS value to set
        border-radius. Numbers are converted to rem.
        `theme.defaultRadius` by default.

    - disabled (boolean; optional):
        Sets `disabled` and `data-disabled` attributes on the button
        element.

    - iconSize (string | number; optional):
        `X` icon `width` and `height`, `80%` by default.

    - children (a list of or a singular dash component, string or number; optional):
        Content rendered inside the button, for example
        `VisuallyHidden` with label for screen readers.

    - icon (a list of or a singular dash component, string or number; optional):
        Replaces default close icon. If set, `iconSize` prop is
        ignored.

    - className (string; optional):
        Class added to the root element, if applicable.

    - style (optional):
        Inline style added to root component element, can subscribe to
        theme defined on MantineProvider.

    - hiddenFrom (optional):
        Breakpoint above which the component is hidden with `display:
        none`.

    - visibleFrom (optional):
        Breakpoint below which the component is hidden with `display:
        none`.

    - lightHidden (boolean; optional):
        Determines whether component should be hidden in light color
        scheme with `display: none`.

    - darkHidden (boolean; optional):
        Determines whether component should be hidden in dark color
        scheme with `display: none`.

    - mod (string; optional):
        Element modifiers transformed into `data-` attributes, for
        example, `{ 'data-size': 'xl' }`, falsy values are removed.

    - m (number; optional):
        Margin, theme key: theme.spacing.

    - my (number; optional):
        MarginBlock, theme key: theme.spacing.

    - mx (number; optional):
        MarginInline, theme key: theme.spacing.

    - mt (number; optional):
        MarginTop, theme key: theme.spacing.

    - mb (number; optional):
        MarginBottom, theme key: theme.spacing.

    - ms (number; optional):
        MarginInlineStart, theme key: theme.spacing.

    - me (number; optional):
        MarginInlineEnd, theme key: theme.spacing.

    - ml (number; optional):
        MarginLeft, theme key: theme.spacing.

    - mr (number; optional):
        MarginRight, theme key: theme.spacing.

    - p (number; optional):
        Padding, theme key: theme.spacing.

    - py (number; optional):
        PaddingBlock, theme key: theme.spacing.

    - px (number; optional):
        PaddingInline, theme key: theme.spacing.

    - pt (number; optional):
        PaddingTop, theme key: theme.spacing.

    - pb (number; optional):
        PaddingBottom, theme key: theme.spacing.

    - ps (number; optional):
        PaddingInlineStart, theme key: theme.spacing.

    - pe (number; optional):
        PaddingInlineEnd, theme key: theme.spacing.

    - pl (number; optional):
        PaddingLeft, theme key: theme.spacing.

    - pr (number; optional):
        PaddingRight, theme key: theme.spacing.

    - bd (string | number; optional):
        Border.

    - bg (optional):
        Background, theme key: theme.colors.

    - c (optional):
        Color.

    - opacity (optional)

    - ff (optional):
        FontFamily.

    - fz (number; optional):
        FontSize, theme key: theme.fontSizes.

    - fw (optional):
        FontWeight.

    - lts (string | number; optional):
        LetterSpacing.

    - ta (optional):
        TextAlign.

    - lh (number; optional):
        LineHeight, theme key: lineHeights.

    - fs (optional):
        FontStyle.

    - tt (optional):
        TextTransform.

    - td (string | number; optional):
        TextDecoration.

    - w (string | number; optional):
        Width, theme key: theme.spacing.

    - miw (string | number; optional):
        MinWidth, theme key: theme.spacing.

    - maw (string | number; optional):
        MaxWidth, theme key: theme.spacing.

    - h (string | number; optional):
        Height, theme key: theme.spacing.

    - mih (string | number; optional):
        MinHeight, theme key: theme.spacing.

    - mah (string | number; optional):
        MaxHeight, theme key: theme.spacing.

    - bgsz (string | number; optional):
        BackgroundSize.

    - bgp (string | number; optional):
        BackgroundPosition.

    - bgr (optional):
        BackgroundRepeat.

    - bga (optional):
        BackgroundAttachment.

    - pos (optional):
        Position.

    - top (string | number; optional)

    - left (string | number; optional)

    - bottom (string | number; optional)

    - right (string | number; optional)

    - inset (string | number; optional)

    - display (optional)

    - flex (string | number; optional)

- closeOnClickOutside (boolean; optional):
    Determines whether the modal/drawer should be closed when user
    clicks on the overlay, `True` by default.

- closeOnEscape (boolean; optional):
    Determines whether `onClose` should be called when user presses
    the escape key, `True` by default.

- darkHidden (boolean; optional):
    Determines whether component should be hidden in dark color scheme
    with `display: none`.

- data-* (string; optional):
    Wild card data attributes.

- display (optional)

- ff (optional):
    FontFamily.

- flex (string | number; optional)

- fs (optional):
    FontStyle.

- fullScreen (boolean; optional):
    Determines whether the modal should take the entire screen,
    `False` by default.

- fw (optional):
    FontWeight.

- fz (number; optional):
    FontSize, theme key: theme.fontSizes.

- h (string | number; optional):
    Height, theme key: theme.spacing.

- hiddenFrom (optional):
    Breakpoint above which the component is hidden with `display:
    none`.

- inset (string | number; optional)

- keepMounted (boolean; optional):
    If set modal/drawer will not be unmounted from the DOM when it is
    hidden, `display: none` styles will be added instead, `False` by
    default.

- left (string | number; optional)

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

- lockScroll (boolean; optional):
    Determines whether scroll should be locked when `opened={True}`,
    `True` by default.

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

- mod (string; optional):
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

- opened (boolean; default False):
    Determines whether modal/drawer is opened.

- overlayProps (dict; optional):
    Props passed down to the `Overlay` component, use to configure
    opacity, `background-color`, styles and other properties.

    `overlayProps` is a dict with keys:

    - transitionProps (dict; optional):
        Props passed down to the `Transition` component.

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

    - className (string; optional):
        Class added to the root element, if applicable.

    - style (optional):
        Inline style added to root component element, can subscribe to
        theme defined on MantineProvider.

    - hiddenFrom (optional):
        Breakpoint above which the component is hidden with `display:
        none`.

    - visibleFrom (optional):
        Breakpoint below which the component is hidden with `display:
        none`.

    - lightHidden (boolean; optional):
        Determines whether component should be hidden in light color
        scheme with `display: none`.

    - darkHidden (boolean; optional):
        Determines whether component should be hidden in dark color
        scheme with `display: none`.

    - mod (string; optional):
        Element modifiers transformed into `data-` attributes, for
        example, `{ 'data-size': 'xl' }`, falsy values are removed.

    - m (number; optional):
        Margin, theme key: theme.spacing.

    - my (number; optional):
        MarginBlock, theme key: theme.spacing.

    - mx (number; optional):
        MarginInline, theme key: theme.spacing.

    - mt (number; optional):
        MarginTop, theme key: theme.spacing.

    - mb (number; optional):
        MarginBottom, theme key: theme.spacing.

    - ms (number; optional):
        MarginInlineStart, theme key: theme.spacing.

    - me (number; optional):
        MarginInlineEnd, theme key: theme.spacing.

    - ml (number; optional):
        MarginLeft, theme key: theme.spacing.

    - mr (number; optional):
        MarginRight, theme key: theme.spacing.

    - p (number; optional):
        Padding, theme key: theme.spacing.

    - py (number; optional):
        PaddingBlock, theme key: theme.spacing.

    - px (number; optional):
        PaddingInline, theme key: theme.spacing.

    - pt (number; optional):
        PaddingTop, theme key: theme.spacing.

    - pb (number; optional):
        PaddingBottom, theme key: theme.spacing.

    - ps (number; optional):
        PaddingInlineStart, theme key: theme.spacing.

    - pe (number; optional):
        PaddingInlineEnd, theme key: theme.spacing.

    - pl (number; optional):
        PaddingLeft, theme key: theme.spacing.

    - pr (number; optional):
        PaddingRight, theme key: theme.spacing.

    - bd (string | number; optional):
        Border.

    - bg (optional):
        Background, theme key: theme.colors.

    - c (optional):
        Color.

    - opacity (optional)

    - ff (optional):
        FontFamily.

    - fz (number; optional):
        FontSize, theme key: theme.fontSizes.

    - fw (optional):
        FontWeight.

    - lts (string | number; optional):
        LetterSpacing.

    - ta (optional):
        TextAlign.

    - lh (number; optional):
        LineHeight, theme key: lineHeights.

    - fs (optional):
        FontStyle.

    - tt (optional):
        TextTransform.

    - td (string | number; optional):
        TextDecoration.

    - w (string | number; optional):
        Width, theme key: theme.spacing.

    - miw (string | number; optional):
        MinWidth, theme key: theme.spacing.

    - maw (string | number; optional):
        MaxWidth, theme key: theme.spacing.

    - h (string | number; optional):
        Height, theme key: theme.spacing.

    - mih (string | number; optional):
        MinHeight, theme key: theme.spacing.

    - mah (string | number; optional):
        MaxHeight, theme key: theme.spacing.

    - bgsz (string | number; optional):
        BackgroundSize.

    - bgp (string | number; optional):
        BackgroundPosition.

    - bgr (optional):
        BackgroundRepeat.

    - bga (optional):
        BackgroundAttachment.

    - pos (optional):
        Position.

    - top (string | number; optional)

    - left (string | number; optional)

    - bottom (string | number; optional)

    - right (string | number; optional)

    - inset (string | number; optional)

    - display (optional)

    - flex (string | number; optional)

    - zIndex (string | number; optional):
        Overlay z-index, `200` by default.

    - center (boolean; optional):
        Determines whether content inside overlay should be vertically
        and horizontally centered, `False` by default.

    - fixed (boolean; optional):
        Determines whether overlay should have fixed position instead
        of absolute, `False` by default.

    - children (a list of or a singular dash component, string or number; optional):
        Content inside overlay.

    - radius (number; optional):
        Key of `theme.radius` or any valid CSS value to set
        border-radius, `0` by default.

    - color (optional):
        Overlay `background-color`, `#000` by default.

    - unstyled (boolean; optional):
        Remove all Mantine styling from the component.

    - gradient (string; optional):
        Changes overlay to gradient. If set, `color` prop is ignored.

    - backgroundOpacity (number; optional):
        Controls overlay `background-color` opacity 0–1, disregarded
        when `gradient` prop is set, `0.6` by default.

    - blur (string | number; optional):
        Overlay background blur, `0` by default.

- p (number; optional):
    Padding, theme key: theme.spacing.

- padding (number; optional):
    Key of `theme.spacing` or any valid CSS value to set content,
    header and footer padding, `'md'` by default.

- pb (number; optional):
    PaddingBottom, theme key: theme.spacing.

- pe (number; optional):
    PaddingInlineEnd, theme key: theme.spacing.

- pl (number; optional):
    PaddingLeft, theme key: theme.spacing.

- portalProps (dict; optional):
    Props passed down to the Portal component when `withinPortal` is
    set.

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

- radius (number; optional):
    Key of `theme.radius` or any valid CSS value to set
    `border-radius`, `theme.defaultRadius` by default.

- removeScrollProps (dict; optional):
    Props passed down to react-remove-scroll, can be used to customize
    scroll lock behavior.

- returnFocus (boolean; optional):
    Determines whether focus should be returned to the last active
    element when `onClose` is called, `True` by default.

- right (string | number; optional)

- shadow (optional):
    Key of `theme.shadows` or any valid CSS box-shadow value, 'xl' by
    default.

- size (number; optional):
    Controls width of the content area, `'md'` by default.

- styles (boolean | number | string | dict | list; optional):
    Mantine styles API.

- ta (optional):
    TextAlign.

- tabIndex (number; optional):
    tab-index.

- td (string | number; optional):
    TextDecoration.

- title (a list of or a singular dash component, string or number; optional):
    Modal title.

- top (string | number; optional)

- transitionProps (dict; optional):
    Props added to the `Transition` component that used to animate
    overlay and body, use to configure duration and animation type, `{
    duration: 200, transition: 'pop' }` by default.

    `transitionProps` is a dict with keys:

    - keepMounted (boolean; optional):
        If set element will not be unmounted from the DOM when it is
        hidden, `display: none` styles will be applied instead.

    - transition (optional):
        Transition name or object.

    - duration (number; optional):
        Transition duration in ms, `250` by default.

    - exitDuration (number; optional):
        Exit transition duration in ms, `250` by default.

    - timingFunction (string; optional):
        Transition timing function, `theme.transitionTimingFunction`
        by default.

    - mounted (boolean; required):
        Determines whether component should be mounted to the DOM.

- trapFocus (boolean; optional):
    Determines whether focus should be trapped, `True` by default.

- tt (optional):
    TextTransform.

- unstyled (boolean; optional):
    Remove all Mantine styling from the component.

- variant (string; optional):
    variant.

- visibleFrom (optional):
    Breakpoint below which the component is hidden with `display:
    none`.

- w (string | number; optional):
    Width, theme key: theme.spacing.

- withCloseButton (boolean; optional):
    Determines whether the close button should be rendered, `True` by
    default.

- withOverlay (boolean; optional):
    Determines whether the overlay should be rendered, `True` by
    default.

- withinPortal (boolean; optional):
    Determines whether the component should be rendered inside
    `Portal`, `True` by default.

- xOffset (string | number; optional):
    Left/right modal offset, `5vw` by default.

- yOffset (string | number; optional):
    Top/bottom modal offset, `5dvh` by default.

- zIndex (string | number; optional):
    `z-index` CSS property of the root element, `200` by default."""
    _children_props = ['title', 'overlayProps.children', 'closeButtonProps.children', 'closeButtonProps.icon']
    _base_nodes = ['title', 'children']
    _namespace = 'dash_mantine_components'
    _type = 'Modal'
    OverlayPropsTransitionProps = TypedDict(
        "OverlayPropsTransitionProps",
            {
            "keepMounted": NotRequired[bool],
            "transition": NotRequired[typing.Union[Literal["fade"], Literal["fade-down"], Literal["fade-up"], Literal["fade-left"], Literal["fade-right"], Literal["skew-up"], Literal["skew-down"], Literal["rotate-right"], Literal["rotate-left"], Literal["slide-down"], Literal["slide-up"], Literal["slide-right"], Literal["slide-left"], Literal["scale-y"], Literal["scale-x"], Literal["scale"], Literal["pop"], Literal["pop-top-left"], Literal["pop-top-right"], Literal["pop-bottom-left"], Literal["pop-bottom-right"]]],
            "duration": NotRequired[NumberType],
            "exitDuration": NotRequired[NumberType],
            "timingFunction": NotRequired[str],
            "mounted": bool
        }
    )

    OverlayProps = TypedDict(
        "OverlayProps",
            {
            "transitionProps": NotRequired["OverlayPropsTransitionProps"],
            "className": NotRequired[str],
            "style": NotRequired[typing.Union[typing.Any]],
            "hiddenFrom": NotRequired[typing.Union[Literal["xs"], Literal["sm"], Literal["md"], Literal["lg"], Literal["xl"]]],
            "visibleFrom": NotRequired[typing.Union[Literal["xs"], Literal["sm"], Literal["md"], Literal["lg"], Literal["xl"]]],
            "lightHidden": NotRequired[bool],
            "darkHidden": NotRequired[bool],
            "mod": NotRequired[typing.Union[str]],
            "m": NotRequired[typing.Union[NumberType, Literal["xs"], Literal["sm"], Literal["md"], Literal["lg"], Literal["xl"]]],
            "my": NotRequired[typing.Union[NumberType, Literal["xs"], Literal["sm"], Literal["md"], Literal["lg"], Literal["xl"]]],
            "mx": NotRequired[typing.Union[NumberType, Literal["xs"], Literal["sm"], Literal["md"], Literal["lg"], Literal["xl"]]],
            "mt": NotRequired[typing.Union[NumberType, Literal["xs"], Literal["sm"], Literal["md"], Literal["lg"], Literal["xl"]]],
            "mb": NotRequired[typing.Union[NumberType, Literal["xs"], Literal["sm"], Literal["md"], Literal["lg"], Literal["xl"]]],
            "ms": NotRequired[typing.Union[NumberType, Literal["xs"], Literal["sm"], Literal["md"], Literal["lg"], Literal["xl"]]],
            "me": NotRequired[typing.Union[NumberType, Literal["xs"], Literal["sm"], Literal["md"], Literal["lg"], Literal["xl"]]],
            "ml": NotRequired[typing.Union[NumberType, Literal["xs"], Literal["sm"], Literal["md"], Literal["lg"], Literal["xl"]]],
            "mr": NotRequired[typing.Union[NumberType, Literal["xs"], Literal["sm"], Literal["md"], Literal["lg"], Literal["xl"]]],
            "p": NotRequired[typing.Union[NumberType, Literal["xs"], Literal["sm"], Literal["md"], Literal["lg"], Literal["xl"]]],
            "py": NotRequired[typing.Union[NumberType, Literal["xs"], Literal["sm"], Literal["md"], Literal["lg"], Literal["xl"]]],
            "px": NotRequired[typing.Union[NumberType, Literal["xs"], Literal["sm"], Literal["md"], Literal["lg"], Literal["xl"]]],
            "pt": NotRequired[typing.Union[NumberType, Literal["xs"], Literal["sm"], Literal["md"], Literal["lg"], Literal["xl"]]],
            "pb": NotRequired[typing.Union[NumberType, Literal["xs"], Literal["sm"], Literal["md"], Literal["lg"], Literal["xl"]]],
            "ps": NotRequired[typing.Union[NumberType, Literal["xs"], Literal["sm"], Literal["md"], Literal["lg"], Literal["xl"]]],
            "pe": NotRequired[typing.Union[NumberType, Literal["xs"], Literal["sm"], Literal["md"], Literal["lg"], Literal["xl"]]],
            "pl": NotRequired[typing.Union[NumberType, Literal["xs"], Literal["sm"], Literal["md"], Literal["lg"], Literal["xl"]]],
            "pr": NotRequired[typing.Union[NumberType, Literal["xs"], Literal["sm"], Literal["md"], Literal["lg"], Literal["xl"]]],
            "bd": NotRequired[typing.Union[str, NumberType]],
            "bg": NotRequired[typing.Union[Literal["blue"], Literal["cyan"], Literal["gray"], Literal["green"], Literal["indigo"], Literal["lime"], Literal["orange"], Literal["pink"], Literal["red"], Literal["teal"], Literal["violet"], Literal["yellow"], Literal["dark"], Literal["grape"]]],
            "c": NotRequired[typing.Union[Literal["blue"], Literal["cyan"], Literal["gray"], Literal["green"], Literal["indigo"], Literal["lime"], Literal["orange"], Literal["pink"], Literal["red"], Literal["teal"], Literal["violet"], Literal["yellow"], Literal["dark"], Literal["grape"]]],
            "opacity": NotRequired[typing.Union[Literal["-moz-initial"], Literal["inherit"], Literal["initial"], Literal["revert"], Literal["revert-layer"], Literal["unset"]]],
            "ff": NotRequired[typing.Union[Literal["monospace"], Literal["text"], Literal["heading"]]],
            "fz": NotRequired[typing.Union[NumberType, Literal["xs"], Literal["sm"], Literal["md"], Literal["lg"], Literal["xl"], Literal["h1"], Literal["h2"], Literal["h3"], Literal["h4"], Literal["h5"], Literal["h6"]]],
            "fw": NotRequired[typing.Union[Literal["-moz-initial"], Literal["inherit"], Literal["initial"], Literal["revert"], Literal["revert-layer"], Literal["unset"], Literal["bold"], Literal["normal"], Literal["bolder"], Literal["lighter"]]],
            "lts": NotRequired[typing.Union[str, NumberType]],
            "ta": NotRequired[typing.Union[Literal["left"], Literal["right"], Literal["-moz-initial"], Literal["inherit"], Literal["initial"], Literal["revert"], Literal["revert-layer"], Literal["unset"], Literal["-webkit-match-parent"], Literal["center"], Literal["end"], Literal["justify"], Literal["match-parent"], Literal["start"]]],
            "lh": NotRequired[typing.Union[NumberType, Literal["xs"], Literal["sm"], Literal["md"], Literal["lg"], Literal["xl"], Literal["h1"], Literal["h2"], Literal["h3"], Literal["h4"], Literal["h5"], Literal["h6"]]],
            "fs": NotRequired[typing.Union[Literal["-moz-initial"], Literal["inherit"], Literal["initial"], Literal["revert"], Literal["revert-layer"], Literal["unset"], Literal["normal"], Literal["italic"], Literal["oblique"]]],
            "tt": NotRequired[typing.Union[Literal["-moz-initial"], Literal["inherit"], Literal["initial"], Literal["revert"], Literal["revert-layer"], Literal["unset"], Literal["none"], Literal["capitalize"], Literal["full-size-kana"], Literal["full-width"], Literal["lowercase"], Literal["uppercase"]]],
            "td": NotRequired[typing.Union[str, NumberType]],
            "w": NotRequired[typing.Union[str, NumberType]],
            "miw": NotRequired[typing.Union[str, NumberType]],
            "maw": NotRequired[typing.Union[str, NumberType]],
            "h": NotRequired[typing.Union[str, NumberType]],
            "mih": NotRequired[typing.Union[str, NumberType]],
            "mah": NotRequired[typing.Union[str, NumberType]],
            "bgsz": NotRequired[typing.Union[str, NumberType]],
            "bgp": NotRequired[typing.Union[str, NumberType]],
            "bgr": NotRequired[typing.Union[Literal["-moz-initial"], Literal["inherit"], Literal["initial"], Literal["revert"], Literal["revert-layer"], Literal["unset"], Literal["no-repeat"], Literal["repeat"], Literal["repeat-x"], Literal["repeat-y"], Literal["round"], Literal["space"]]],
            "bga": NotRequired[typing.Union[Literal["-moz-initial"], Literal["inherit"], Literal["initial"], Literal["revert"], Literal["revert-layer"], Literal["unset"], Literal["fixed"], Literal["local"], Literal["scroll"]]],
            "pos": NotRequired[typing.Union[Literal["-moz-initial"], Literal["inherit"], Literal["initial"], Literal["revert"], Literal["revert-layer"], Literal["unset"], Literal["fixed"], Literal["-webkit-sticky"], Literal["absolute"], Literal["relative"], Literal["static"], Literal["sticky"]]],
            "top": NotRequired[typing.Union[str, NumberType]],
            "left": NotRequired[typing.Union[str, NumberType]],
            "bottom": NotRequired[typing.Union[str, NumberType]],
            "right": NotRequired[typing.Union[str, NumberType]],
            "inset": NotRequired[typing.Union[str, NumberType]],
            "display": NotRequired[typing.Union[Literal["flex"], Literal["-moz-initial"], Literal["inherit"], Literal["initial"], Literal["revert"], Literal["revert-layer"], Literal["unset"], Literal["none"], Literal["block"], Literal["inline"], Literal["run-in"], Literal["-ms-flexbox"], Literal["-ms-grid"], Literal["-webkit-flex"], Literal["flow"], Literal["flow-root"], Literal["grid"], Literal["ruby"], Literal["table"], Literal["ruby-base"], Literal["ruby-base-container"], Literal["ruby-text"], Literal["ruby-text-container"], Literal["table-caption"], Literal["table-cell"], Literal["table-column"], Literal["table-column-group"], Literal["table-footer-group"], Literal["table-header-group"], Literal["table-row"], Literal["table-row-group"], Literal["-ms-inline-flexbox"], Literal["-ms-inline-grid"], Literal["-webkit-inline-flex"], Literal["inline-block"], Literal["inline-flex"], Literal["inline-grid"], Literal["inline-list-item"], Literal["inline-table"], Literal["contents"], Literal["list-item"]]],
            "flex": NotRequired[typing.Union[str, NumberType]],
            "zIndex": NotRequired[typing.Union[str, NumberType]],
            "center": NotRequired[bool],
            "fixed": NotRequired[bool],
            "children": NotRequired[ComponentType],
            "radius": NotRequired[typing.Union[NumberType, Literal["xs"], Literal["sm"], Literal["md"], Literal["lg"], Literal["xl"]]],
            "color": NotRequired[typing.Union[Literal["-moz-initial"], Literal["inherit"], Literal["initial"], Literal["revert"], Literal["revert-layer"], Literal["unset"], Literal["aliceblue"], Literal["antiquewhite"], Literal["aqua"], Literal["aquamarine"], Literal["azure"], Literal["beige"], Literal["bisque"], Literal["black"], Literal["blanchedalmond"], Literal["blue"], Literal["blueviolet"], Literal["brown"], Literal["burlywood"], Literal["cadetblue"], Literal["chartreuse"], Literal["chocolate"], Literal["coral"], Literal["cornflowerblue"], Literal["cornsilk"], Literal["crimson"], Literal["cyan"], Literal["darkblue"], Literal["darkcyan"], Literal["darkgoldenrod"], Literal["darkgray"], Literal["darkgreen"], Literal["darkgrey"], Literal["darkkhaki"], Literal["darkmagenta"], Literal["darkolivegreen"], Literal["darkorange"], Literal["darkorchid"], Literal["darkred"], Literal["darksalmon"], Literal["darkseagreen"], Literal["darkslateblue"], Literal["darkslategray"], Literal["darkslategrey"], Literal["darkturquoise"], Literal["darkviolet"], Literal["deeppink"], Literal["deepskyblue"], Literal["dimgray"], Literal["dimgrey"], Literal["dodgerblue"], Literal["firebrick"], Literal["floralwhite"], Literal["forestgreen"], Literal["fuchsia"], Literal["gainsboro"], Literal["ghostwhite"], Literal["gold"], Literal["goldenrod"], Literal["gray"], Literal["green"], Literal["greenyellow"], Literal["grey"], Literal["honeydew"], Literal["hotpink"], Literal["indianred"], Literal["indigo"], Literal["ivory"], Literal["khaki"], Literal["lavender"], Literal["lavenderblush"], Literal["lawngreen"], Literal["lemonchiffon"], Literal["lightblue"], Literal["lightcoral"], Literal["lightcyan"], Literal["lightgoldenrodyellow"], Literal["lightgray"], Literal["lightgreen"], Literal["lightgrey"], Literal["lightpink"], Literal["lightsalmon"], Literal["lightseagreen"], Literal["lightskyblue"], Literal["lightslategray"], Literal["lightslategrey"], Literal["lightsteelblue"], Literal["lightyellow"], Literal["lime"], Literal["limegreen"], Literal["linen"], Literal["magenta"], Literal["maroon"], Literal["mediumaquamarine"], Literal["mediumblue"], Literal["mediumorchid"], Literal["mediumpurple"], Literal["mediumseagreen"], Literal["mediumslateblue"], Literal["mediumspringgreen"], Literal["mediumturquoise"], Literal["mediumvioletred"], Literal["midnightblue"], Literal["mintcream"], Literal["mistyrose"], Literal["moccasin"], Literal["navajowhite"], Literal["navy"], Literal["oldlace"], Literal["olive"], Literal["olivedrab"], Literal["orange"], Literal["orangered"], Literal["orchid"], Literal["palegoldenrod"], Literal["palegreen"], Literal["paleturquoise"], Literal["palevioletred"], Literal["papayawhip"], Literal["peachpuff"], Literal["peru"], Literal["pink"], Literal["plum"], Literal["powderblue"], Literal["purple"], Literal["rebeccapurple"], Literal["red"], Literal["rosybrown"], Literal["royalblue"], Literal["saddlebrown"], Literal["salmon"], Literal["sandybrown"], Literal["seagreen"], Literal["seashell"], Literal["sienna"], Literal["silver"], Literal["skyblue"], Literal["slateblue"], Literal["slategray"], Literal["slategrey"], Literal["snow"], Literal["springgreen"], Literal["steelblue"], Literal["tan"], Literal["teal"], Literal["thistle"], Literal["tomato"], Literal["transparent"], Literal["turquoise"], Literal["violet"], Literal["wheat"], Literal["white"], Literal["whitesmoke"], Literal["yellow"], Literal["yellowgreen"], Literal["ActiveBorder"], Literal["ActiveCaption"], Literal["AppWorkspace"], Literal["Background"], Literal["ButtonFace"], Literal["ButtonHighlight"], Literal["ButtonShadow"], Literal["ButtonText"], Literal["CaptionText"], Literal["GrayText"], Literal["Highlight"], Literal["HighlightText"], Literal["InactiveBorder"], Literal["InactiveCaption"], Literal["InactiveCaptionText"], Literal["InfoBackground"], Literal["InfoText"], Literal["Menu"], Literal["MenuText"], Literal["Scrollbar"], Literal["ThreeDDarkShadow"], Literal["ThreeDFace"], Literal["ThreeDHighlight"], Literal["ThreeDLightShadow"], Literal["ThreeDShadow"], Literal["Window"], Literal["WindowFrame"], Literal["WindowText"], Literal["currentcolor"]]],
            "unstyled": NotRequired[bool],
            "gradient": NotRequired[str],
            "backgroundOpacity": NotRequired[NumberType],
            "blur": NotRequired[typing.Union[str, NumberType]]
        }
    )

    CloseButtonProps = TypedDict(
        "CloseButtonProps",
            {
            "size": NotRequired[typing.Union[NumberType, Literal["xs"], Literal["sm"], Literal["md"], Literal["lg"], Literal["xl"]]],
            "radius": NotRequired[typing.Union[NumberType, Literal["xs"], Literal["sm"], Literal["md"], Literal["lg"], Literal["xl"]]],
            "disabled": NotRequired[bool],
            "iconSize": NotRequired[typing.Union[str, NumberType]],
            "children": NotRequired[ComponentType],
            "icon": NotRequired[ComponentType],
            "className": NotRequired[str],
            "style": NotRequired[typing.Union[typing.Any]],
            "hiddenFrom": NotRequired[typing.Union[Literal["xs"], Literal["sm"], Literal["md"], Literal["lg"], Literal["xl"]]],
            "visibleFrom": NotRequired[typing.Union[Literal["xs"], Literal["sm"], Literal["md"], Literal["lg"], Literal["xl"]]],
            "lightHidden": NotRequired[bool],
            "darkHidden": NotRequired[bool],
            "mod": NotRequired[typing.Union[str]],
            "m": NotRequired[typing.Union[NumberType, Literal["xs"], Literal["sm"], Literal["md"], Literal["lg"], Literal["xl"]]],
            "my": NotRequired[typing.Union[NumberType, Literal["xs"], Literal["sm"], Literal["md"], Literal["lg"], Literal["xl"]]],
            "mx": NotRequired[typing.Union[NumberType, Literal["xs"], Literal["sm"], Literal["md"], Literal["lg"], Literal["xl"]]],
            "mt": NotRequired[typing.Union[NumberType, Literal["xs"], Literal["sm"], Literal["md"], Literal["lg"], Literal["xl"]]],
            "mb": NotRequired[typing.Union[NumberType, Literal["xs"], Literal["sm"], Literal["md"], Literal["lg"], Literal["xl"]]],
            "ms": NotRequired[typing.Union[NumberType, Literal["xs"], Literal["sm"], Literal["md"], Literal["lg"], Literal["xl"]]],
            "me": NotRequired[typing.Union[NumberType, Literal["xs"], Literal["sm"], Literal["md"], Literal["lg"], Literal["xl"]]],
            "ml": NotRequired[typing.Union[NumberType, Literal["xs"], Literal["sm"], Literal["md"], Literal["lg"], Literal["xl"]]],
            "mr": NotRequired[typing.Union[NumberType, Literal["xs"], Literal["sm"], Literal["md"], Literal["lg"], Literal["xl"]]],
            "p": NotRequired[typing.Union[NumberType, Literal["xs"], Literal["sm"], Literal["md"], Literal["lg"], Literal["xl"]]],
            "py": NotRequired[typing.Union[NumberType, Literal["xs"], Literal["sm"], Literal["md"], Literal["lg"], Literal["xl"]]],
            "px": NotRequired[typing.Union[NumberType, Literal["xs"], Literal["sm"], Literal["md"], Literal["lg"], Literal["xl"]]],
            "pt": NotRequired[typing.Union[NumberType, Literal["xs"], Literal["sm"], Literal["md"], Literal["lg"], Literal["xl"]]],
            "pb": NotRequired[typing.Union[NumberType, Literal["xs"], Literal["sm"], Literal["md"], Literal["lg"], Literal["xl"]]],
            "ps": NotRequired[typing.Union[NumberType, Literal["xs"], Literal["sm"], Literal["md"], Literal["lg"], Literal["xl"]]],
            "pe": NotRequired[typing.Union[NumberType, Literal["xs"], Literal["sm"], Literal["md"], Literal["lg"], Literal["xl"]]],
            "pl": NotRequired[typing.Union[NumberType, Literal["xs"], Literal["sm"], Literal["md"], Literal["lg"], Literal["xl"]]],
            "pr": NotRequired[typing.Union[NumberType, Literal["xs"], Literal["sm"], Literal["md"], Literal["lg"], Literal["xl"]]],
            "bd": NotRequired[typing.Union[str, NumberType]],
            "bg": NotRequired[typing.Union[Literal["blue"], Literal["cyan"], Literal["gray"], Literal["green"], Literal["indigo"], Literal["lime"], Literal["orange"], Literal["pink"], Literal["red"], Literal["teal"], Literal["violet"], Literal["yellow"], Literal["dark"], Literal["grape"]]],
            "c": NotRequired[typing.Union[Literal["blue"], Literal["cyan"], Literal["gray"], Literal["green"], Literal["indigo"], Literal["lime"], Literal["orange"], Literal["pink"], Literal["red"], Literal["teal"], Literal["violet"], Literal["yellow"], Literal["dark"], Literal["grape"]]],
            "opacity": NotRequired[typing.Union[Literal["-moz-initial"], Literal["inherit"], Literal["initial"], Literal["revert"], Literal["revert-layer"], Literal["unset"]]],
            "ff": NotRequired[typing.Union[Literal["monospace"], Literal["text"], Literal["heading"]]],
            "fz": NotRequired[typing.Union[NumberType, Literal["xs"], Literal["sm"], Literal["md"], Literal["lg"], Literal["xl"], Literal["h1"], Literal["h2"], Literal["h3"], Literal["h4"], Literal["h5"], Literal["h6"]]],
            "fw": NotRequired[typing.Union[Literal["-moz-initial"], Literal["inherit"], Literal["initial"], Literal["revert"], Literal["revert-layer"], Literal["unset"], Literal["bold"], Literal["normal"], Literal["bolder"], Literal["lighter"]]],
            "lts": NotRequired[typing.Union[str, NumberType]],
            "ta": NotRequired[typing.Union[Literal["left"], Literal["right"], Literal["-moz-initial"], Literal["inherit"], Literal["initial"], Literal["revert"], Literal["revert-layer"], Literal["unset"], Literal["-webkit-match-parent"], Literal["center"], Literal["end"], Literal["justify"], Literal["match-parent"], Literal["start"]]],
            "lh": NotRequired[typing.Union[NumberType, Literal["xs"], Literal["sm"], Literal["md"], Literal["lg"], Literal["xl"], Literal["h1"], Literal["h2"], Literal["h3"], Literal["h4"], Literal["h5"], Literal["h6"]]],
            "fs": NotRequired[typing.Union[Literal["-moz-initial"], Literal["inherit"], Literal["initial"], Literal["revert"], Literal["revert-layer"], Literal["unset"], Literal["normal"], Literal["italic"], Literal["oblique"]]],
            "tt": NotRequired[typing.Union[Literal["-moz-initial"], Literal["inherit"], Literal["initial"], Literal["revert"], Literal["revert-layer"], Literal["unset"], Literal["none"], Literal["capitalize"], Literal["full-size-kana"], Literal["full-width"], Literal["lowercase"], Literal["uppercase"]]],
            "td": NotRequired[typing.Union[str, NumberType]],
            "w": NotRequired[typing.Union[str, NumberType]],
            "miw": NotRequired[typing.Union[str, NumberType]],
            "maw": NotRequired[typing.Union[str, NumberType]],
            "h": NotRequired[typing.Union[str, NumberType]],
            "mih": NotRequired[typing.Union[str, NumberType]],
            "mah": NotRequired[typing.Union[str, NumberType]],
            "bgsz": NotRequired[typing.Union[str, NumberType]],
            "bgp": NotRequired[typing.Union[str, NumberType]],
            "bgr": NotRequired[typing.Union[Literal["-moz-initial"], Literal["inherit"], Literal["initial"], Literal["revert"], Literal["revert-layer"], Literal["unset"], Literal["no-repeat"], Literal["repeat"], Literal["repeat-x"], Literal["repeat-y"], Literal["round"], Literal["space"]]],
            "bga": NotRequired[typing.Union[Literal["-moz-initial"], Literal["inherit"], Literal["initial"], Literal["revert"], Literal["revert-layer"], Literal["unset"], Literal["fixed"], Literal["local"], Literal["scroll"]]],
            "pos": NotRequired[typing.Union[Literal["-moz-initial"], Literal["inherit"], Literal["initial"], Literal["revert"], Literal["revert-layer"], Literal["unset"], Literal["fixed"], Literal["-webkit-sticky"], Literal["absolute"], Literal["relative"], Literal["static"], Literal["sticky"]]],
            "top": NotRequired[typing.Union[str, NumberType]],
            "left": NotRequired[typing.Union[str, NumberType]],
            "bottom": NotRequired[typing.Union[str, NumberType]],
            "right": NotRequired[typing.Union[str, NumberType]],
            "inset": NotRequired[typing.Union[str, NumberType]],
            "display": NotRequired[typing.Union[Literal["flex"], Literal["-moz-initial"], Literal["inherit"], Literal["initial"], Literal["revert"], Literal["revert-layer"], Literal["unset"], Literal["none"], Literal["block"], Literal["inline"], Literal["run-in"], Literal["-ms-flexbox"], Literal["-ms-grid"], Literal["-webkit-flex"], Literal["flow"], Literal["flow-root"], Literal["grid"], Literal["ruby"], Literal["table"], Literal["ruby-base"], Literal["ruby-base-container"], Literal["ruby-text"], Literal["ruby-text-container"], Literal["table-caption"], Literal["table-cell"], Literal["table-column"], Literal["table-column-group"], Literal["table-footer-group"], Literal["table-header-group"], Literal["table-row"], Literal["table-row-group"], Literal["-ms-inline-flexbox"], Literal["-ms-inline-grid"], Literal["-webkit-inline-flex"], Literal["inline-block"], Literal["inline-flex"], Literal["inline-grid"], Literal["inline-list-item"], Literal["inline-table"], Literal["contents"], Literal["list-item"]]],
            "flex": NotRequired[typing.Union[str, NumberType]]
        }
    )

    TransitionProps = TypedDict(
        "TransitionProps",
            {
            "keepMounted": NotRequired[bool],
            "transition": NotRequired[typing.Union[Literal["fade"], Literal["fade-down"], Literal["fade-up"], Literal["fade-left"], Literal["fade-right"], Literal["skew-up"], Literal["skew-down"], Literal["rotate-right"], Literal["rotate-left"], Literal["slide-down"], Literal["slide-up"], Literal["slide-right"], Literal["slide-left"], Literal["scale-y"], Literal["scale-x"], Literal["scale"], Literal["pop"], Literal["pop-top-left"], Literal["pop-top-right"], Literal["pop-bottom-left"], Literal["pop-bottom-right"]]],
            "duration": NotRequired[NumberType],
            "exitDuration": NotRequired[NumberType],
            "timingFunction": NotRequired[str],
            "mounted": bool
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
        title: typing.Optional[ComponentType] = None,
        withOverlay: typing.Optional[bool] = None,
        overlayProps: typing.Optional["OverlayProps"] = None,
        withCloseButton: typing.Optional[bool] = None,
        closeButtonProps: typing.Optional["CloseButtonProps"] = None,
        yOffset: typing.Optional[typing.Union[str, NumberType]] = None,
        xOffset: typing.Optional[typing.Union[str, NumberType]] = None,
        radius: typing.Optional[typing.Union[NumberType, Literal["xs"], Literal["sm"], Literal["md"], Literal["lg"], Literal["xl"]]] = None,
        centered: typing.Optional[bool] = None,
        fullScreen: typing.Optional[bool] = None,
        keepMounted: typing.Optional[bool] = None,
        opened: typing.Optional[bool] = None,
        lockScroll: typing.Optional[bool] = None,
        trapFocus: typing.Optional[bool] = None,
        withinPortal: typing.Optional[bool] = None,
        portalProps: typing.Optional[dict] = None,
        closeOnClickOutside: typing.Optional[bool] = None,
        transitionProps: typing.Optional["TransitionProps"] = None,
        closeOnEscape: typing.Optional[bool] = None,
        returnFocus: typing.Optional[bool] = None,
        zIndex: typing.Optional[typing.Union[str, NumberType]] = None,
        shadow: typing.Optional[typing.Union[Literal["xs"], Literal["sm"], Literal["md"], Literal["lg"], Literal["xl"]]] = None,
        padding: typing.Optional[typing.Union[NumberType, Literal["xs"], Literal["sm"], Literal["md"], Literal["lg"], Literal["xl"]]] = None,
        size: typing.Optional[typing.Union[NumberType, Literal["xs"], Literal["sm"], Literal["md"], Literal["lg"], Literal["xl"]]] = None,
        removeScrollProps: typing.Optional[dict] = None,
        className: typing.Optional[str] = None,
        style: typing.Optional[typing.Any] = None,
        hiddenFrom: typing.Optional[typing.Union[Literal["xs"], Literal["sm"], Literal["md"], Literal["lg"], Literal["xl"]]] = None,
        visibleFrom: typing.Optional[typing.Union[Literal["xs"], Literal["sm"], Literal["md"], Literal["lg"], Literal["xl"]]] = None,
        lightHidden: typing.Optional[bool] = None,
        darkHidden: typing.Optional[bool] = None,
        mod: typing.Optional[typing.Union[str]] = None,
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
        classNames: typing.Optional[dict] = None,
        styles: typing.Optional[typing.Any] = None,
        unstyled: typing.Optional[bool] = None,
        variant: typing.Optional[str] = None,
        id: typing.Optional[typing.Union[str, dict]] = None,
        tabIndex: typing.Optional[NumberType] = None,
        loading_state: typing.Optional["LoadingState"] = None,
        **kwargs
    ):
        self._prop_names = ['children', 'id', 'aria-*', 'bd', 'bg', 'bga', 'bgp', 'bgr', 'bgsz', 'bottom', 'c', 'centered', 'className', 'classNames', 'closeButtonProps', 'closeOnClickOutside', 'closeOnEscape', 'darkHidden', 'data-*', 'display', 'ff', 'flex', 'fs', 'fullScreen', 'fw', 'fz', 'h', 'hiddenFrom', 'inset', 'keepMounted', 'left', 'lh', 'lightHidden', 'loading_state', 'lockScroll', 'lts', 'm', 'mah', 'maw', 'mb', 'me', 'mih', 'miw', 'ml', 'mod', 'mr', 'ms', 'mt', 'mx', 'my', 'opacity', 'opened', 'overlayProps', 'p', 'padding', 'pb', 'pe', 'pl', 'portalProps', 'pos', 'pr', 'ps', 'pt', 'px', 'py', 'radius', 'removeScrollProps', 'returnFocus', 'right', 'shadow', 'size', 'style', 'styles', 'ta', 'tabIndex', 'td', 'title', 'top', 'transitionProps', 'trapFocus', 'tt', 'unstyled', 'variant', 'visibleFrom', 'w', 'withCloseButton', 'withOverlay', 'withinPortal', 'xOffset', 'yOffset', 'zIndex']
        self._valid_wildcard_attributes =            ['data-', 'aria-']
        self.available_properties = ['children', 'id', 'aria-*', 'bd', 'bg', 'bga', 'bgp', 'bgr', 'bgsz', 'bottom', 'c', 'centered', 'className', 'classNames', 'closeButtonProps', 'closeOnClickOutside', 'closeOnEscape', 'darkHidden', 'data-*', 'display', 'ff', 'flex', 'fs', 'fullScreen', 'fw', 'fz', 'h', 'hiddenFrom', 'inset', 'keepMounted', 'left', 'lh', 'lightHidden', 'loading_state', 'lockScroll', 'lts', 'm', 'mah', 'maw', 'mb', 'me', 'mih', 'miw', 'ml', 'mod', 'mr', 'ms', 'mt', 'mx', 'my', 'opacity', 'opened', 'overlayProps', 'p', 'padding', 'pb', 'pe', 'pl', 'portalProps', 'pos', 'pr', 'ps', 'pt', 'px', 'py', 'radius', 'removeScrollProps', 'returnFocus', 'right', 'shadow', 'size', 'style', 'styles', 'ta', 'tabIndex', 'td', 'title', 'top', 'transitionProps', 'trapFocus', 'tt', 'unstyled', 'variant', 'visibleFrom', 'w', 'withCloseButton', 'withOverlay', 'withinPortal', 'xOffset', 'yOffset', 'zIndex']
        self.available_wildcard_properties =            ['data-', 'aria-']
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(Modal, self).__init__(children=children, **args)

setattr(Modal, "__init__", _explicitize_args(Modal.__init__))
