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


class YearPickerInput(Component):
    """A YearPickerInput component.
YearPickerInput

Keyword arguments:

- id (string; optional):
    Unique ID to identify this component in Dash callbacks.

- allowDeselect (boolean; optional):
    Determines whether user can deselect the date by clicking on
    selected item, applicable only when type=\"default\".

- allowSingleDateInRange (boolean; optional):
    Determines whether single year can be selected as range,
    applicable only when type=\"range\".

- aria-* (string; optional):
    Wild card aria attributes.

- ariaLabels (dict; optional):
    aria-label attributes for controls on different levels.

    `ariaLabels` is a dict with keys:

    - monthLevelControl (string; optional)

    - yearLevelControl (string; optional)

    - nextMonth (string; optional)

    - previousMonth (string; optional)

    - nextYear (string; optional)

    - previousYear (string; optional)

    - nextDecade (string; optional)

    - previousDecade (string; optional)

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

- clearButtonProps (dict; optional):
    Props passed down to clear button.

    `clearButtonProps` is a dict with keys:

    - size (optional):
        Size of the button, by default value is based on input
        context.

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

- clearable (boolean; optional):
    Determines whether input value can be cleared, adds clear button
    to right section, False by default.

- closeOnChange (boolean; optional):
    Determines whether dropdown should be closed when date is
    selected, not applicable when type=\"multiple\", True by default.

- columnsToScroll (number; optional):
    Number of columns to scroll when user clicks next/prev buttons,
    defaults to numberOfColumns.

- darkHidden (boolean; optional):
    Determines whether component should be hidden in dark color scheme
    with `display: none`.

- data-* (string; optional):
    Wild card data attributes.

- debounce (number; default 0):
    Debounce time in ms.

- decadeLabelFormat (string; optional):
    dayjs label format to display decade label or a function that
    returns decade label based on date value, defaults to \"YYYY\".

- description (a list of or a singular dash component, string or number; optional):
    Contents of `Input.Description` component. If not set, description
    is not rendered.

- descriptionProps (dict with strings as keys and values of type boolean | number | string | dict | list; optional):
    Props passed down to the `Input.Description` component.

- disabled (boolean; optional):
    Sets `disabled` attribute on the `input` element.

- display (optional)

- dropdownType (a value equal to: 'popover', 'modal'; optional):
    Type of dropdown, defaults to popover.

- error (a list of or a singular dash component, string or number; optional):
    Contents of `Input.Error` component. If not set, error is not
    rendered.

- errorProps (dict with strings as keys and values of type boolean | number | string | dict | list; optional):
    Props passed down to the `Input.Error` component.

- ff (optional):
    FontFamily.

- firstDayOfWeek (a value equal to: 0, 1, 2, 3, 4, 5, 6; optional):
    number 0-6, 0 – Sunday, 6 – Saturday, defaults to 1 – Monday.

- flex (string | number; optional)

- fs (optional):
    FontStyle.

- fw (optional):
    FontWeight.

- fz (number; optional):
    FontSize, theme key: theme.fontSizes.

- h (string | number; optional):
    Height, theme key: theme.spacing.

- hasNextLevel (boolean; optional):
    Determines whether next level button should be enabled, defaults
    to True.

- hiddenFrom (optional):
    Breakpoint above which the component is hidden with `display:
    none`.

- hideOutsideDates (boolean; optional):
    Determines whether outside dates should be hidden, defaults to
    False.

- hideWeekdays (boolean; optional):
    Determines whether weekdays row should be hidden, defaults to
    False.

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

- labelSeparator (string; optional):
    Separator between range value.

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

- level (a value equal to: 'month', 'year', 'decade'; optional):
    Current level displayed to the user (decade, year, month), used
    for controlled component.

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

- maxDate (string; optional):
    Maximum possible date.

- mb (number; optional):
    MarginBottom, theme key: theme.spacing.

- me (number; optional):
    MarginInlineEnd, theme key: theme.spacing.

- mih (string | number; optional):
    MinHeight, theme key: theme.spacing.

- minDate (string; optional):
    Minimum possible date.

- miw (string | number; optional):
    MinWidth, theme key: theme.spacing.

- ml (number; optional):
    MarginLeft, theme key: theme.spacing.

- mod (string | dict with strings as keys and values of type boolean | number | string | dict | list; optional):
    Element modifiers transformed into `data-` attributes, for
    example, `{ 'data-size': 'xl' }`, falsy values are removed.

- modalProps (dict; optional):
    Props passed down to Modal component.

    `modalProps` is a dict with keys:

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

    - mod (string | dict with strings as keys and values of type boolean | number | string | dict | list; optional):
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

    - size (number; optional):
        Controls width of the content area, `'md'` by default.

    - radius (number; optional):
        Key of `theme.radius` or any valid CSS value to set
        `border-radius`, `theme.defaultRadius` by default.

    - opened (boolean; optional):
        Determines whether modal/drawer is opened.

    - closeOnClickOutside (boolean; optional):
        Determines whether the modal/drawer should be closed when user
        clicks on the overlay, `True` by default.

    - trapFocus (boolean; optional):
        Determines whether focus should be trapped, `True` by default.

    - closeOnEscape (boolean; optional):
        Determines whether `onClose` should be called when user
        presses the escape key, `True` by default.

    - keepMounted (boolean; optional):
        If set modal/drawer will not be unmounted from the DOM when it
        is hidden, `display: none` styles will be added instead,
        `False` by default.

    - transitionProps (dict; optional):
        Props added to the `Transition` component that used to animate
        overlay and body, use to configure duration and animation
        type, `{ duration: 200, transition: 'pop' }` by default.

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

    - withinPortal (boolean; optional):
        Determines whether the component should be rendered inside
        `Portal`, `True` by default.

    - portalProps (dict; optional):
        Props passed down to the Portal component when `withinPortal`
        is set.

    - zIndex (string | number; optional):
        `z-index` CSS property of the root element, `200` by default.

    - shadow (optional):
        Key of `theme.shadows` or any valid CSS box-shadow value, 'xl'
        by default.

    - returnFocus (boolean; optional):
        Determines whether focus should be returned to the last active
        element when `onClose` is called, `True` by default.

    - overlayProps (dict; optional):
        Props passed down to the `Overlay` component, use to configure
        opacity, `background-color`, styles and other properties.

        `overlayProps` is a dict with keys:

        - transitionProps (dict; optional):
            Props passed down to the `Transition` component.

            `transitionProps` is a dict with keys:

            - keepMounted (boolean; optional):
                If set element will not be unmounted from the DOM when
                it is hidden, `display: none` styles will be applied
                instead.

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
                Determines whether component should be mounted to the
                DOM.

        - className (string; optional):
            Class added to the root element, if applicable.

        - style (optional):
            Inline style added to root component element, can
            subscribe to theme defined on MantineProvider.

        - hiddenFrom (optional):
            Breakpoint above which the component is hidden with
            `display: none`.

        - visibleFrom (optional):
            Breakpoint below which the component is hidden with
            `display: none`.

        - lightHidden (boolean; optional):
            Determines whether component should be hidden in light
            color scheme with `display: none`.

        - darkHidden (boolean; optional):
            Determines whether component should be hidden in dark
            color scheme with `display: none`.

        - mod (string | dict with strings as keys and values of type boolean | number | string | dict | list; optional):
            Element modifiers transformed into `data-` attributes, for
            example, `{ 'data-size': 'xl' }`, falsy values are
            removed.

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

        - radius (number; optional):
            Key of `theme.radius` or any valid CSS value to set
            border-radius, `0` by default.

        - unstyled (boolean; optional):
            Remove all Mantine styling from the component.

        - children (a list of or a singular dash component, string or number; optional):
            Content inside overlay.

        - zIndex (string | number; optional):
            Overlay z-index, `200` by default.

        - center (boolean; optional):
            Determines whether content inside overlay should be
            vertically and horizontally centered, `False` by default.

        - fixed (boolean; optional):
            Determines whether overlay should have fixed position
            instead of absolute, `False` by default.

        - backgroundOpacity (number; optional):
            Controls overlay `background-color` opacity 0–1,
            disregarded when `gradient` prop is set, `0.6` by default.

        - color (optional):
            Overlay `background-color`, `#000` by default.

        - blur (string | number; optional):
            Overlay background blur, `0` by default.

        - gradient (string; optional):
            Changes overlay to gradient. If set, `color` prop is
            ignored.

    - withOverlay (boolean; optional):
        Determines whether the overlay should be rendered, `True` by
        default.

    - padding (number; optional):
        Key of `theme.spacing` or any valid CSS value to set content,
        header and footer padding, `'md'` by default.

    - title (a list of or a singular dash component, string or number; optional):
        Modal title.

    - withCloseButton (boolean; optional):
        Determines whether the close button should be rendered, `True`
        by default.

    - closeButtonProps (dict; optional):
        Props passed down to the close button.

        `closeButtonProps` is a dict with keys:

        - size (number; optional):
            Controls width and height of the button. Numbers are
            converted to rem. `'md'` by default.

        - radius (number; optional):
            Key of `theme.radius` or any valid CSS value to set
            border-radius. Numbers are converted to rem.
            `theme.defaultRadius` by default.

        - disabled (boolean; optional):
            Sets `disabled` and `data-disabled` attributes on the
            button element.

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
            Inline style added to root component element, can
            subscribe to theme defined on MantineProvider.

        - hiddenFrom (optional):
            Breakpoint above which the component is hidden with
            `display: none`.

        - visibleFrom (optional):
            Breakpoint below which the component is hidden with
            `display: none`.

        - lightHidden (boolean; optional):
            Determines whether component should be hidden in light
            color scheme with `display: none`.

        - darkHidden (boolean; optional):
            Determines whether component should be hidden in dark
            color scheme with `display: none`.

        - mod (string | dict with strings as keys and values of type boolean | number | string | dict | list; optional):
            Element modifiers transformed into `data-` attributes, for
            example, `{ 'data-size': 'xl' }`, falsy values are
            removed.

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

    - yOffset (string | number; optional):
        Top/bottom modal offset, `5dvh` by default.

    - xOffset (string | number; optional):
        Left/right modal offset, `5vw` by default.

    - centered (boolean; optional):
        Determines whether the modal should be centered vertically,
        `False` by default.

    - fullScreen (boolean; optional):
        Determines whether the modal should take the entire screen,
        `False` by default.

    - lockScroll (boolean; optional):
        Determines whether scroll should be locked when
        `opened={True}`, `True` by default.

    - removeScrollProps (dict; optional):
        Props passed down to react-remove-scroll, can be used to
        customize scroll lock behavior.

- monthLabelFormat (string; optional):
    dayjs label format to display month label or a function that
    returns month label based on month value, defaults to \"MMMM
    YYYY\".

- monthsListFormat (string; optional):
    dayjs format for months list.

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

- n_submit (number; default 0):
    An integer that represents the number of times that this element
    has been submitted.

- name (string; optional):
    Name prop.

- nextIcon (a list of or a singular dash component, string or number; optional):
    Change next icon.

- nextLabel (string; optional):
    aria-label for next button.

- numberOfColumns (number; optional):
    Number of columns to render next to each other.

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
    Input placeholder.

- pointer (boolean; optional):
    Determines whether the input should have `cursor: pointer` style,
    `False` by default.

- popoverProps (dict; optional):
    Props passed down to Popover component.

    `popoverProps` is a dict with keys:

    - radius (number; optional):
        Key of `theme.radius` or any valid CSS value to set
        border-radius, `theme.defaultRadius` by default.

    - disabled (boolean; optional):
        If set, popover dropdown will not be rendered.

    - classNames (dict; optional):
        Adds class names to Mantine components.

    - styles (boolean | number | string | dict | list; optional):
        Mantine styles API.

    - unstyled (boolean; optional):
        Remove all Mantine styling from the component.

    - variant (string; optional):
        variant.

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

    - shadow (optional):
        Key of `theme.shadows` or any other valid CSS `box-shadow`
        value.

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

- pos (optional):
    Position.

- pr (number; optional):
    PaddingRight, theme key: theme.spacing.

- previousIcon (a list of or a singular dash component, string or number; optional):
    Change previous icon.

- previousLabel (string; optional):
    aria-label for previous button.

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
    Determines whether the user can modify the value.

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

- size (a value equal to: 'xs', 'sm', 'md', 'lg', 'xl'; optional):
    Component size.

- sortDates (boolean; optional):
    Determines whether dates value should be sorted before onChange
    call, only applicable when type=\"multiple\", True by default.

- styles (boolean | number | string | dict | list; optional):
    Mantine styles API.

- ta (optional):
    TextAlign.

- tabIndex (number; optional):
    tab-index.

- td (string | number; optional):
    TextDecoration.

- top (string | number; optional)

- tt (optional):
    TextTransform.

- type (a value equal to: 'default', 'multiple', 'range'; optional):
    Picker type: range, multiple or default.

- unstyled (boolean; optional):
    Remove all Mantine styling from the component.

- value (string | list of strings; optional):
    Value for controlled component.

- valueFormat (string; optional):
    Dayjs format to display input value, \"MMMM D, YYYY\" by default.

- variant (string; optional):
    variant.

- visibleFrom (optional):
    Breakpoint below which the component is hidden with `display:
    none`.

- w (string | number; optional):
    Width, theme key: theme.spacing.

- weekdayFormat (string; optional):
    dayjs format for weekdays names, defaults to \"dd\".

- weekendDays (list of a value equal to: 0, 1, 2, 3, 4, 5, 6s; optional):
    Indices of weekend days, 0-6, where 0 is Sunday and 6 is Saturday,
    defaults to value defined in DatesProvider.

- withAsterisk (boolean; optional):
    Determines whether the required asterisk should be displayed.
    Overrides `required` prop. Does not add required attribute to the
    input. `False` by default.

- withCellSpacing (boolean; optional):
    Determines whether controls should be separated by spacing, True
    by default.

- withErrorStyles (boolean; optional):
    Determines whether the input should have red border and red text
    color when the `error` prop is set, `True` by default.

- withWeekNumbers (boolean; optional):
    Determines whether week numbers should be displayed, False by
    default.

- wrapperProps (dict with strings as keys and values of type boolean | number | string | dict | list; optional):
    Props passed down to the root element.

- yearLabelFormat (string; optional):
    dayjs label format to display year label or a function that
    returns year label based on year value, defaults to \"YYYY\".

- yearsListFormat (string; optional):
    dayjs format for years list, `'YYYY'` by default."""
    _children_props = ['popoverProps.middlewares.flip.boundary', 'modalProps.overlayProps.children', 'modalProps.title', 'modalProps.closeButtonProps.children', 'modalProps.closeButtonProps.icon', 'clearButtonProps.children', 'clearButtonProps.icon', 'leftSection', 'rightSection', 'label', 'description', 'error', 'nextIcon', 'previousIcon']
    _base_nodes = ['leftSection', 'rightSection', 'label', 'description', 'error', 'nextIcon', 'previousIcon', 'children']
    _namespace = 'dash_mantine_components'
    _type = 'YearPickerInput'
    LoadingState = TypedDict(
        "LoadingState",
            {
            "is_loading": bool,
            "prop_name": str,
            "component_name": str
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
            "radius": NotRequired[typing.Union[NumberType, Literal["xs"], Literal["sm"], Literal["md"], Literal["lg"], Literal["xl"]]],
            "disabled": NotRequired[bool],
            "classNames": NotRequired[dict],
            "styles": NotRequired[typing.Any],
            "unstyled": NotRequired[bool],
            "variant": NotRequired[str],
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
            "shadow": NotRequired[typing.Union[Literal["xs"], Literal["sm"], Literal["md"], Literal["lg"], Literal["xl"]]],
            "returnFocus": NotRequired[bool],
            "floatingStrategy": NotRequired[Literal["absolute", "fixed"]],
            "overlayProps": NotRequired[dict],
            "withOverlay": NotRequired[bool]
        }
    )

    ModalPropsTransitionProps = TypedDict(
        "ModalPropsTransitionProps",
            {
            "keepMounted": NotRequired[bool],
            "transition": NotRequired[typing.Union[Literal["fade"], Literal["fade-down"], Literal["fade-up"], Literal["fade-left"], Literal["fade-right"], Literal["skew-up"], Literal["skew-down"], Literal["rotate-right"], Literal["rotate-left"], Literal["slide-down"], Literal["slide-up"], Literal["slide-right"], Literal["slide-left"], Literal["scale-y"], Literal["scale-x"], Literal["scale"], Literal["pop"], Literal["pop-top-left"], Literal["pop-top-right"], Literal["pop-bottom-left"], Literal["pop-bottom-right"]]],
            "duration": NotRequired[NumberType],
            "exitDuration": NotRequired[NumberType],
            "timingFunction": NotRequired[str],
            "mounted": bool
        }
    )

    ModalPropsOverlayPropsTransitionProps = TypedDict(
        "ModalPropsOverlayPropsTransitionProps",
            {
            "keepMounted": NotRequired[bool],
            "transition": NotRequired[typing.Union[Literal["fade"], Literal["fade-down"], Literal["fade-up"], Literal["fade-left"], Literal["fade-right"], Literal["skew-up"], Literal["skew-down"], Literal["rotate-right"], Literal["rotate-left"], Literal["slide-down"], Literal["slide-up"], Literal["slide-right"], Literal["slide-left"], Literal["scale-y"], Literal["scale-x"], Literal["scale"], Literal["pop"], Literal["pop-top-left"], Literal["pop-top-right"], Literal["pop-bottom-left"], Literal["pop-bottom-right"]]],
            "duration": NotRequired[NumberType],
            "exitDuration": NotRequired[NumberType],
            "timingFunction": NotRequired[str],
            "mounted": bool
        }
    )

    ModalPropsOverlayProps = TypedDict(
        "ModalPropsOverlayProps",
            {
            "transitionProps": NotRequired["ModalPropsOverlayPropsTransitionProps"],
            "className": NotRequired[str],
            "style": NotRequired[typing.Union[typing.Any]],
            "hiddenFrom": NotRequired[typing.Union[Literal["xs"], Literal["sm"], Literal["md"], Literal["lg"], Literal["xl"]]],
            "visibleFrom": NotRequired[typing.Union[Literal["xs"], Literal["sm"], Literal["md"], Literal["lg"], Literal["xl"]]],
            "lightHidden": NotRequired[bool],
            "darkHidden": NotRequired[bool],
            "mod": NotRequired[typing.Union[str, typing.Dict[typing.Union[str, float, int], typing.Any]]],
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
            "ta": NotRequired[typing.Union[Literal["left"], Literal["right"], Literal["end"], Literal["start"], Literal["-moz-initial"], Literal["inherit"], Literal["initial"], Literal["revert"], Literal["revert-layer"], Literal["unset"], Literal["center"], Literal["-webkit-match-parent"], Literal["justify"], Literal["match-parent"]]],
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
            "bga": NotRequired[typing.Union[Literal["local"], Literal["-moz-initial"], Literal["inherit"], Literal["initial"], Literal["revert"], Literal["revert-layer"], Literal["unset"], Literal["fixed"], Literal["scroll"]]],
            "pos": NotRequired[typing.Union[Literal["-moz-initial"], Literal["inherit"], Literal["initial"], Literal["revert"], Literal["revert-layer"], Literal["unset"], Literal["absolute"], Literal["fixed"], Literal["-webkit-sticky"], Literal["relative"], Literal["static"], Literal["sticky"]]],
            "top": NotRequired[typing.Union[str, NumberType]],
            "left": NotRequired[typing.Union[str, NumberType]],
            "bottom": NotRequired[typing.Union[str, NumberType]],
            "right": NotRequired[typing.Union[str, NumberType]],
            "inset": NotRequired[typing.Union[str, NumberType]],
            "display": NotRequired[typing.Union[Literal["flex"], Literal["-moz-initial"], Literal["inherit"], Literal["initial"], Literal["revert"], Literal["revert-layer"], Literal["unset"], Literal["none"], Literal["block"], Literal["inline"], Literal["run-in"], Literal["-ms-flexbox"], Literal["-ms-grid"], Literal["-webkit-flex"], Literal["flow"], Literal["flow-root"], Literal["grid"], Literal["ruby"], Literal["table"], Literal["ruby-base"], Literal["ruby-base-container"], Literal["ruby-text"], Literal["ruby-text-container"], Literal["table-caption"], Literal["table-cell"], Literal["table-column"], Literal["table-column-group"], Literal["table-footer-group"], Literal["table-header-group"], Literal["table-row"], Literal["table-row-group"], Literal["-ms-inline-flexbox"], Literal["-ms-inline-grid"], Literal["-webkit-inline-flex"], Literal["inline-block"], Literal["inline-flex"], Literal["inline-grid"], Literal["inline-list-item"], Literal["inline-table"], Literal["contents"], Literal["list-item"]]],
            "flex": NotRequired[typing.Union[str, NumberType]],
            "radius": NotRequired[typing.Union[NumberType, Literal["xs"], Literal["sm"], Literal["md"], Literal["lg"], Literal["xl"]]],
            "unstyled": NotRequired[bool],
            "children": NotRequired[ComponentType],
            "zIndex": NotRequired[typing.Union[str, NumberType]],
            "center": NotRequired[bool],
            "fixed": NotRequired[bool],
            "backgroundOpacity": NotRequired[NumberType],
            "color": NotRequired[typing.Union[Literal["-moz-initial"], Literal["inherit"], Literal["initial"], Literal["revert"], Literal["revert-layer"], Literal["unset"], Literal["aliceblue"], Literal["antiquewhite"], Literal["aqua"], Literal["aquamarine"], Literal["azure"], Literal["beige"], Literal["bisque"], Literal["black"], Literal["blanchedalmond"], Literal["blue"], Literal["blueviolet"], Literal["brown"], Literal["burlywood"], Literal["cadetblue"], Literal["chartreuse"], Literal["chocolate"], Literal["coral"], Literal["cornflowerblue"], Literal["cornsilk"], Literal["crimson"], Literal["cyan"], Literal["darkblue"], Literal["darkcyan"], Literal["darkgoldenrod"], Literal["darkgray"], Literal["darkgreen"], Literal["darkgrey"], Literal["darkkhaki"], Literal["darkmagenta"], Literal["darkolivegreen"], Literal["darkorange"], Literal["darkorchid"], Literal["darkred"], Literal["darksalmon"], Literal["darkseagreen"], Literal["darkslateblue"], Literal["darkslategray"], Literal["darkslategrey"], Literal["darkturquoise"], Literal["darkviolet"], Literal["deeppink"], Literal["deepskyblue"], Literal["dimgray"], Literal["dimgrey"], Literal["dodgerblue"], Literal["firebrick"], Literal["floralwhite"], Literal["forestgreen"], Literal["fuchsia"], Literal["gainsboro"], Literal["ghostwhite"], Literal["gold"], Literal["goldenrod"], Literal["gray"], Literal["green"], Literal["greenyellow"], Literal["grey"], Literal["honeydew"], Literal["hotpink"], Literal["indianred"], Literal["indigo"], Literal["ivory"], Literal["khaki"], Literal["lavender"], Literal["lavenderblush"], Literal["lawngreen"], Literal["lemonchiffon"], Literal["lightblue"], Literal["lightcoral"], Literal["lightcyan"], Literal["lightgoldenrodyellow"], Literal["lightgray"], Literal["lightgreen"], Literal["lightgrey"], Literal["lightpink"], Literal["lightsalmon"], Literal["lightseagreen"], Literal["lightskyblue"], Literal["lightslategray"], Literal["lightslategrey"], Literal["lightsteelblue"], Literal["lightyellow"], Literal["lime"], Literal["limegreen"], Literal["linen"], Literal["magenta"], Literal["maroon"], Literal["mediumaquamarine"], Literal["mediumblue"], Literal["mediumorchid"], Literal["mediumpurple"], Literal["mediumseagreen"], Literal["mediumslateblue"], Literal["mediumspringgreen"], Literal["mediumturquoise"], Literal["mediumvioletred"], Literal["midnightblue"], Literal["mintcream"], Literal["mistyrose"], Literal["moccasin"], Literal["navajowhite"], Literal["navy"], Literal["oldlace"], Literal["olive"], Literal["olivedrab"], Literal["orange"], Literal["orangered"], Literal["orchid"], Literal["palegoldenrod"], Literal["palegreen"], Literal["paleturquoise"], Literal["palevioletred"], Literal["papayawhip"], Literal["peachpuff"], Literal["peru"], Literal["pink"], Literal["plum"], Literal["powderblue"], Literal["purple"], Literal["rebeccapurple"], Literal["red"], Literal["rosybrown"], Literal["royalblue"], Literal["saddlebrown"], Literal["salmon"], Literal["sandybrown"], Literal["seagreen"], Literal["seashell"], Literal["sienna"], Literal["silver"], Literal["skyblue"], Literal["slateblue"], Literal["slategray"], Literal["slategrey"], Literal["snow"], Literal["springgreen"], Literal["steelblue"], Literal["tan"], Literal["teal"], Literal["thistle"], Literal["tomato"], Literal["transparent"], Literal["turquoise"], Literal["violet"], Literal["wheat"], Literal["white"], Literal["whitesmoke"], Literal["yellow"], Literal["yellowgreen"], Literal["ActiveBorder"], Literal["ActiveCaption"], Literal["AppWorkspace"], Literal["Background"], Literal["ButtonFace"], Literal["ButtonHighlight"], Literal["ButtonShadow"], Literal["ButtonText"], Literal["CaptionText"], Literal["GrayText"], Literal["Highlight"], Literal["HighlightText"], Literal["InactiveBorder"], Literal["InactiveCaption"], Literal["InactiveCaptionText"], Literal["InfoBackground"], Literal["InfoText"], Literal["Menu"], Literal["MenuText"], Literal["Scrollbar"], Literal["ThreeDDarkShadow"], Literal["ThreeDFace"], Literal["ThreeDHighlight"], Literal["ThreeDLightShadow"], Literal["ThreeDShadow"], Literal["Window"], Literal["WindowFrame"], Literal["WindowText"], Literal["currentcolor"]]],
            "blur": NotRequired[typing.Union[str, NumberType]],
            "gradient": NotRequired[str]
        }
    )

    ModalPropsCloseButtonProps = TypedDict(
        "ModalPropsCloseButtonProps",
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
            "mod": NotRequired[typing.Union[str, typing.Dict[typing.Union[str, float, int], typing.Any]]],
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
            "ta": NotRequired[typing.Union[Literal["left"], Literal["right"], Literal["end"], Literal["start"], Literal["-moz-initial"], Literal["inherit"], Literal["initial"], Literal["revert"], Literal["revert-layer"], Literal["unset"], Literal["center"], Literal["-webkit-match-parent"], Literal["justify"], Literal["match-parent"]]],
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
            "bga": NotRequired[typing.Union[Literal["local"], Literal["-moz-initial"], Literal["inherit"], Literal["initial"], Literal["revert"], Literal["revert-layer"], Literal["unset"], Literal["fixed"], Literal["scroll"]]],
            "pos": NotRequired[typing.Union[Literal["-moz-initial"], Literal["inherit"], Literal["initial"], Literal["revert"], Literal["revert-layer"], Literal["unset"], Literal["absolute"], Literal["fixed"], Literal["-webkit-sticky"], Literal["relative"], Literal["static"], Literal["sticky"]]],
            "top": NotRequired[typing.Union[str, NumberType]],
            "left": NotRequired[typing.Union[str, NumberType]],
            "bottom": NotRequired[typing.Union[str, NumberType]],
            "right": NotRequired[typing.Union[str, NumberType]],
            "inset": NotRequired[typing.Union[str, NumberType]],
            "display": NotRequired[typing.Union[Literal["flex"], Literal["-moz-initial"], Literal["inherit"], Literal["initial"], Literal["revert"], Literal["revert-layer"], Literal["unset"], Literal["none"], Literal["block"], Literal["inline"], Literal["run-in"], Literal["-ms-flexbox"], Literal["-ms-grid"], Literal["-webkit-flex"], Literal["flow"], Literal["flow-root"], Literal["grid"], Literal["ruby"], Literal["table"], Literal["ruby-base"], Literal["ruby-base-container"], Literal["ruby-text"], Literal["ruby-text-container"], Literal["table-caption"], Literal["table-cell"], Literal["table-column"], Literal["table-column-group"], Literal["table-footer-group"], Literal["table-header-group"], Literal["table-row"], Literal["table-row-group"], Literal["-ms-inline-flexbox"], Literal["-ms-inline-grid"], Literal["-webkit-inline-flex"], Literal["inline-block"], Literal["inline-flex"], Literal["inline-grid"], Literal["inline-list-item"], Literal["inline-table"], Literal["contents"], Literal["list-item"]]],
            "flex": NotRequired[typing.Union[str, NumberType]]
        }
    )

    ModalProps = TypedDict(
        "ModalProps",
            {
            "className": NotRequired[str],
            "style": NotRequired[typing.Union[typing.Any]],
            "hiddenFrom": NotRequired[typing.Union[Literal["xs"], Literal["sm"], Literal["md"], Literal["lg"], Literal["xl"]]],
            "visibleFrom": NotRequired[typing.Union[Literal["xs"], Literal["sm"], Literal["md"], Literal["lg"], Literal["xl"]]],
            "lightHidden": NotRequired[bool],
            "darkHidden": NotRequired[bool],
            "mod": NotRequired[typing.Union[str, typing.Dict[typing.Union[str, float, int], typing.Any]]],
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
            "ta": NotRequired[typing.Union[Literal["left"], Literal["right"], Literal["end"], Literal["start"], Literal["-moz-initial"], Literal["inherit"], Literal["initial"], Literal["revert"], Literal["revert-layer"], Literal["unset"], Literal["center"], Literal["-webkit-match-parent"], Literal["justify"], Literal["match-parent"]]],
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
            "bga": NotRequired[typing.Union[Literal["local"], Literal["-moz-initial"], Literal["inherit"], Literal["initial"], Literal["revert"], Literal["revert-layer"], Literal["unset"], Literal["fixed"], Literal["scroll"]]],
            "pos": NotRequired[typing.Union[Literal["-moz-initial"], Literal["inherit"], Literal["initial"], Literal["revert"], Literal["revert-layer"], Literal["unset"], Literal["absolute"], Literal["fixed"], Literal["-webkit-sticky"], Literal["relative"], Literal["static"], Literal["sticky"]]],
            "top": NotRequired[typing.Union[str, NumberType]],
            "left": NotRequired[typing.Union[str, NumberType]],
            "bottom": NotRequired[typing.Union[str, NumberType]],
            "right": NotRequired[typing.Union[str, NumberType]],
            "inset": NotRequired[typing.Union[str, NumberType]],
            "display": NotRequired[typing.Union[Literal["flex"], Literal["-moz-initial"], Literal["inherit"], Literal["initial"], Literal["revert"], Literal["revert-layer"], Literal["unset"], Literal["none"], Literal["block"], Literal["inline"], Literal["run-in"], Literal["-ms-flexbox"], Literal["-ms-grid"], Literal["-webkit-flex"], Literal["flow"], Literal["flow-root"], Literal["grid"], Literal["ruby"], Literal["table"], Literal["ruby-base"], Literal["ruby-base-container"], Literal["ruby-text"], Literal["ruby-text-container"], Literal["table-caption"], Literal["table-cell"], Literal["table-column"], Literal["table-column-group"], Literal["table-footer-group"], Literal["table-header-group"], Literal["table-row"], Literal["table-row-group"], Literal["-ms-inline-flexbox"], Literal["-ms-inline-grid"], Literal["-webkit-inline-flex"], Literal["inline-block"], Literal["inline-flex"], Literal["inline-grid"], Literal["inline-list-item"], Literal["inline-table"], Literal["contents"], Literal["list-item"]]],
            "flex": NotRequired[typing.Union[str, NumberType]],
            "size": NotRequired[typing.Union[NumberType, Literal["xs"], Literal["sm"], Literal["md"], Literal["lg"], Literal["xl"]]],
            "radius": NotRequired[typing.Union[NumberType, Literal["xs"], Literal["sm"], Literal["md"], Literal["lg"], Literal["xl"]]],
            "opened": NotRequired[bool],
            "closeOnClickOutside": NotRequired[bool],
            "trapFocus": NotRequired[bool],
            "closeOnEscape": NotRequired[bool],
            "keepMounted": NotRequired[bool],
            "transitionProps": NotRequired["ModalPropsTransitionProps"],
            "withinPortal": NotRequired[bool],
            "portalProps": NotRequired[dict],
            "zIndex": NotRequired[typing.Union[str, NumberType]],
            "shadow": NotRequired[typing.Union[Literal["xs"], Literal["sm"], Literal["md"], Literal["lg"], Literal["xl"]]],
            "returnFocus": NotRequired[bool],
            "overlayProps": NotRequired["ModalPropsOverlayProps"],
            "withOverlay": NotRequired[bool],
            "padding": NotRequired[typing.Union[NumberType, Literal["xs"], Literal["sm"], Literal["md"], Literal["lg"], Literal["xl"]]],
            "title": NotRequired[ComponentType],
            "withCloseButton": NotRequired[bool],
            "closeButtonProps": NotRequired["ModalPropsCloseButtonProps"],
            "yOffset": NotRequired[typing.Union[str, NumberType]],
            "xOffset": NotRequired[typing.Union[str, NumberType]],
            "centered": NotRequired[bool],
            "fullScreen": NotRequired[bool],
            "lockScroll": NotRequired[bool],
            "removeScrollProps": NotRequired[dict]
        }
    )

    ClearButtonProps = TypedDict(
        "ClearButtonProps",
            {
            "size": NotRequired[typing.Union[Literal["xs"], Literal["sm"], Literal["md"], Literal["lg"], Literal["xl"]]],
            "radius": NotRequired[typing.Union[NumberType, Literal["xs"], Literal["sm"], Literal["md"], Literal["lg"], Literal["xl"]]],
            "disabled": NotRequired[bool],
            "iconSize": NotRequired[typing.Union[str, NumberType]],
            "children": NotRequired[ComponentType],
            "icon": NotRequired[ComponentType]
        }
    )

    AriaLabels = TypedDict(
        "AriaLabels",
            {
            "monthLevelControl": NotRequired[str],
            "yearLevelControl": NotRequired[str],
            "nextMonth": NotRequired[str],
            "previousMonth": NotRequired[str],
            "nextYear": NotRequired[str],
            "previousYear": NotRequired[str],
            "nextDecade": NotRequired[str],
            "previousDecade": NotRequired[str]
        }
    )


    def __init__(
        self,
        valueFormat: typing.Optional[str] = None,
        n_submit: typing.Optional[NumberType] = None,
        debounce: typing.Optional[NumberType] = None,
        id: typing.Optional[typing.Union[str, dict]] = None,
        tabIndex: typing.Optional[NumberType] = None,
        loading_state: typing.Optional["LoadingState"] = None,
        persistence: typing.Optional[typing.Union[str, NumberType]] = None,
        persisted_props: typing.Optional[typing.Sequence[str]] = None,
        persistence_type: typing.Optional[Literal["local", "session", "memory"]] = None,
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
        closeOnChange: typing.Optional[bool] = None,
        dropdownType: typing.Optional[Literal["popover", "modal"]] = None,
        popoverProps: typing.Optional["PopoverProps"] = None,
        modalProps: typing.Optional["ModalProps"] = None,
        clearable: typing.Optional[bool] = None,
        clearButtonProps: typing.Optional["ClearButtonProps"] = None,
        readOnly: typing.Optional[bool] = None,
        sortDates: typing.Optional[bool] = None,
        labelSeparator: typing.Optional[str] = None,
        placeholder: typing.Optional[str] = None,
        wrapperProps: typing.Optional[typing.Dict[typing.Union[str, float, int], typing.Any]] = None,
        leftSection: typing.Optional[ComponentType] = None,
        leftSectionWidth: typing.Optional[typing.Union[str, NumberType]] = None,
        leftSectionProps: typing.Optional[dict] = None,
        leftSectionPointerEvents: typing.Optional[Literal["-moz-initial", "inherit", "initial", "revert", "revert-layer", "unset", "auto", "none", "all", "fill", "painted", "stroke", "visible", "visibleFill", "visiblePainted", "visibleStroke"]] = None,
        rightSection: typing.Optional[ComponentType] = None,
        rightSectionWidth: typing.Optional[typing.Union[str, NumberType]] = None,
        rightSectionProps: typing.Optional[dict] = None,
        rightSectionPointerEvents: typing.Optional[Literal["-moz-initial", "inherit", "initial", "revert", "revert-layer", "unset", "auto", "none", "all", "fill", "painted", "stroke", "visible", "visibleFill", "visiblePainted", "visibleStroke"]] = None,
        required: typing.Optional[bool] = None,
        radius: typing.Optional[typing.Union[NumberType, Literal["xs"], Literal["sm"], Literal["md"], Literal["lg"], Literal["xl"]]] = None,
        disabled: typing.Optional[bool] = None,
        pointer: typing.Optional[bool] = None,
        withErrorStyles: typing.Optional[bool] = None,
        name: typing.Optional[str] = None,
        inputProps: typing.Optional[typing.Dict[typing.Union[str, float, int], typing.Any]] = None,
        label: typing.Optional[ComponentType] = None,
        description: typing.Optional[ComponentType] = None,
        error: typing.Optional[ComponentType] = None,
        withAsterisk: typing.Optional[bool] = None,
        labelProps: typing.Optional[typing.Dict[typing.Union[str, float, int], typing.Any]] = None,
        descriptionProps: typing.Optional[typing.Dict[typing.Union[str, float, int], typing.Any]] = None,
        errorProps: typing.Optional[typing.Dict[typing.Union[str, float, int], typing.Any]] = None,
        inputWrapperOrder: typing.Optional[typing.Sequence[Literal["label", "description", "error", "input"]]] = None,
        type: typing.Optional[Literal["default", "multiple", "range"]] = None,
        value: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        allowDeselect: typing.Optional[bool] = None,
        allowSingleDateInRange: typing.Optional[bool] = None,
        decadeLabelFormat: typing.Optional[str] = None,
        yearsListFormat: typing.Optional[str] = None,
        size: typing.Optional[Literal["xs", "sm", "md", "lg", "xl"]] = None,
        withCellSpacing: typing.Optional[bool] = None,
        minDate: typing.Optional[str] = None,
        maxDate: typing.Optional[str] = None,
        numberOfColumns: typing.Optional[NumberType] = None,
        columnsToScroll: typing.Optional[NumberType] = None,
        ariaLabels: typing.Optional["AriaLabels"] = None,
        level: typing.Optional[Literal["month", "year", "decade"]] = None,
        nextIcon: typing.Optional[ComponentType] = None,
        previousIcon: typing.Optional[ComponentType] = None,
        nextLabel: typing.Optional[str] = None,
        previousLabel: typing.Optional[str] = None,
        hasNextLevel: typing.Optional[bool] = None,
        yearLabelFormat: typing.Optional[str] = None,
        monthsListFormat: typing.Optional[str] = None,
        monthLabelFormat: typing.Optional[str] = None,
        firstDayOfWeek: typing.Optional[Literal[0, 1, 2, 3, 4, 5, 6]] = None,
        weekdayFormat: typing.Optional[str] = None,
        weekendDays: typing.Optional[typing.Sequence[Literal[0, 1, 2, 3, 4, 5, 6]]] = None,
        hideOutsideDates: typing.Optional[bool] = None,
        hideWeekdays: typing.Optional[bool] = None,
        withWeekNumbers: typing.Optional[bool] = None,
        classNames: typing.Optional[dict] = None,
        styles: typing.Optional[typing.Any] = None,
        unstyled: typing.Optional[bool] = None,
        variant: typing.Optional[str] = None,
        **kwargs
    ):
        self._prop_names = ['id', 'allowDeselect', 'allowSingleDateInRange', 'aria-*', 'ariaLabels', 'bd', 'bg', 'bga', 'bgp', 'bgr', 'bgsz', 'bottom', 'c', 'className', 'classNames', 'clearButtonProps', 'clearable', 'closeOnChange', 'columnsToScroll', 'darkHidden', 'data-*', 'debounce', 'decadeLabelFormat', 'description', 'descriptionProps', 'disabled', 'display', 'dropdownType', 'error', 'errorProps', 'ff', 'firstDayOfWeek', 'flex', 'fs', 'fw', 'fz', 'h', 'hasNextLevel', 'hiddenFrom', 'hideOutsideDates', 'hideWeekdays', 'inputProps', 'inputWrapperOrder', 'inset', 'label', 'labelProps', 'labelSeparator', 'left', 'leftSection', 'leftSectionPointerEvents', 'leftSectionProps', 'leftSectionWidth', 'level', 'lh', 'lightHidden', 'loading_state', 'lts', 'm', 'mah', 'maw', 'maxDate', 'mb', 'me', 'mih', 'minDate', 'miw', 'ml', 'mod', 'modalProps', 'monthLabelFormat', 'monthsListFormat', 'mr', 'ms', 'mt', 'mx', 'my', 'n_submit', 'name', 'nextIcon', 'nextLabel', 'numberOfColumns', 'opacity', 'p', 'pb', 'pe', 'persisted_props', 'persistence', 'persistence_type', 'pl', 'placeholder', 'pointer', 'popoverProps', 'pos', 'pr', 'previousIcon', 'previousLabel', 'ps', 'pt', 'px', 'py', 'radius', 'readOnly', 'required', 'right', 'rightSection', 'rightSectionPointerEvents', 'rightSectionProps', 'rightSectionWidth', 'size', 'sortDates', 'style', 'styles', 'ta', 'tabIndex', 'td', 'top', 'tt', 'type', 'unstyled', 'value', 'valueFormat', 'variant', 'visibleFrom', 'w', 'weekdayFormat', 'weekendDays', 'withAsterisk', 'withCellSpacing', 'withErrorStyles', 'withWeekNumbers', 'wrapperProps', 'yearLabelFormat', 'yearsListFormat']
        self._valid_wildcard_attributes =            ['data-', 'aria-']
        self.available_properties = ['id', 'allowDeselect', 'allowSingleDateInRange', 'aria-*', 'ariaLabels', 'bd', 'bg', 'bga', 'bgp', 'bgr', 'bgsz', 'bottom', 'c', 'className', 'classNames', 'clearButtonProps', 'clearable', 'closeOnChange', 'columnsToScroll', 'darkHidden', 'data-*', 'debounce', 'decadeLabelFormat', 'description', 'descriptionProps', 'disabled', 'display', 'dropdownType', 'error', 'errorProps', 'ff', 'firstDayOfWeek', 'flex', 'fs', 'fw', 'fz', 'h', 'hasNextLevel', 'hiddenFrom', 'hideOutsideDates', 'hideWeekdays', 'inputProps', 'inputWrapperOrder', 'inset', 'label', 'labelProps', 'labelSeparator', 'left', 'leftSection', 'leftSectionPointerEvents', 'leftSectionProps', 'leftSectionWidth', 'level', 'lh', 'lightHidden', 'loading_state', 'lts', 'm', 'mah', 'maw', 'maxDate', 'mb', 'me', 'mih', 'minDate', 'miw', 'ml', 'mod', 'modalProps', 'monthLabelFormat', 'monthsListFormat', 'mr', 'ms', 'mt', 'mx', 'my', 'n_submit', 'name', 'nextIcon', 'nextLabel', 'numberOfColumns', 'opacity', 'p', 'pb', 'pe', 'persisted_props', 'persistence', 'persistence_type', 'pl', 'placeholder', 'pointer', 'popoverProps', 'pos', 'pr', 'previousIcon', 'previousLabel', 'ps', 'pt', 'px', 'py', 'radius', 'readOnly', 'required', 'right', 'rightSection', 'rightSectionPointerEvents', 'rightSectionProps', 'rightSectionWidth', 'size', 'sortDates', 'style', 'styles', 'ta', 'tabIndex', 'td', 'top', 'tt', 'type', 'unstyled', 'value', 'valueFormat', 'variant', 'visibleFrom', 'w', 'weekdayFormat', 'weekendDays', 'withAsterisk', 'withCellSpacing', 'withErrorStyles', 'withWeekNumbers', 'wrapperProps', 'yearLabelFormat', 'yearsListFormat']
        self.available_wildcard_properties =            ['data-', 'aria-']
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(YearPickerInput, self).__init__(**args)

setattr(YearPickerInput, "__init__", _explicitize_args(YearPickerInput.__init__))
