import React from 'react';

// Professional, reusable Button component in React with TypeScript

import React from 'react';

// Define possible button variants
type ButtonVariant = 'primary' | 'secondary' | 'danger';

// Define possible button sizes
type ButtonSize = 'sm' | 'md' | 'lg';

// Define the props for the Button component
interface ButtonProps extends React.ButtonHTMLAttributes<HTMLButtonElement> {
  /** Variant of the button: primary, secondary, or danger */
  variant?: ButtonVariant;
  /** Button size: sm, md, or lg */
  size?: ButtonSize;
  /** Indicates whether the button is disabled */
  disabled?: boolean;
  /** Called when the button is clicked */
  onClick?: (event: React.MouseEvent<HTMLButtonElement>) => void;
  /** If true, shows a spinner and disables the button */
  loading?: boolean;
  /** Button content */
  children: React.ReactNode;
}

// Helper function to get class names based on props
const getButtonClass = (variant: ButtonVariant, size: ButtonSize, disabled?: boolean): string => {
  const base = 'btn';
  const variantClass = `btn-${variant}`;
  const sizeClass = `btn-${size}`;
  const disabledClass = disabled ? 'btn-disabled' : '';
  return [base, variantClass, sizeClass, disabledClass].join(' ').trim();
};

// Simple Spinner component for loading state
const Spinner: React.FC = () => (
  <span
    role="status"
    aria-live="polite"
    aria-label="Loading"
    style={{ 
      display: 'inline-block', 
      verticalAlign: 'middle', 
      border: '2px solid #f3f3f3',
      borderTop: '2px solid #333', 
      borderRadius: '50%', 
      width: '1em', 
      height: '1em', 
      animation: 'spin 0.8s linear infinite', 
      marginRight: '0.5em'
    }}
  />
);

// Add keyframes for spinner animation
const styles = `
@keyframes spin {
  to { transform: rotate(360deg); }
}
`;
if (typeof window !== "undefined") {
  // Inject the spinner keyframes into the document head only once
  if (!document.getElementById('__button-spinner-keyframes')) {
    const styleEl = document.createElement('style');
    styleEl.id = '__button-spinner-keyframes';
    styleEl.innerHTML = styles;
    document.head.appendChild(styleEl);
  }
}

/**
 * Button component supporting variants, sizes, disabled, and loading states.
 * Applies ARIA attributes for accessibility and is fully typed.
 */
export const Button: React.FC<ButtonProps> = ({
  variant = 'primary',
  size = 'md',
  disabled = false,
  loading = false,
  onClick,
  children,
  ...rest
}) => {
  // If loading, button should be disabled and have proper aria attributes
  const isDisabled = disabled || loading;

  return (
    <button
      type="button"
      className={getButtonClass(variant, size, isDisabled)}
      disabled={isDisabled}
      onClick={isDisabled ? undefined : onClick}
      aria-disabled={isDisabled}
      aria-busy={loading}
      {...rest}
    >
      {/* Show spinner when loading */}
      {loading && <Spinner />}
      {/* Wrap children in a span for layout consistency with or without spinner */}
      <span>{children}</span>
    </button>
  );
};

/*
  Example CSS classes to be provided by your stylesheet:

  .btn {
    font-family: inherit;
    font-weight: 500;
    border: none;
    cursor: pointer;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    transition: background 0.15s;
    border-radius: 4px;
    outline: none;
  }
  .btn-primary   { background: #007bff; color: #fff; }
  .btn-secondary { background: #6c757d; color: #fff; }
  .btn-danger    { background: #dc3545; color: #fff; }
  .btn-sm { padding: 0.25em 0.6em; font-size: 0.875rem; }
  .btn-md { padding: 0.5em 1.2em; font-size: 1rem; }
  .btn-lg { padding: 0.75em 1.8em; font-size: 1.25rem; }
  .btn-disabled, .btn[disabled] {
    background: #e2e6ea;
    color: #adb5bd;
    cursor: not-allowed;
  }
*/
